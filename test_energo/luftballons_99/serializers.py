from importlib.resources import read_binary
from venv import create
from rest_framework import serializers

from .models import LuftBallons, LuftBallonsGuess


# получение шаров 
class LuftBallonsListSerializer(serializers.Serializer):

   ball = serializers.IntegerField(read_only=True)
   id = serializers.IntegerField(read_only=True)
   update = serializers.IntegerField(read_only=True)
   guessed = serializers.BooleanField(read_only=True)




# создание набора шаров
class LuftBallonsSerializer(serializers.Serializer):
   ball = serializers.IntegerField(read_only=True)
   update = serializers.IntegerField(read_only=True)

   def create(self, validated_data):
      # создаем список шаров
      # перемешиваем их
      from random import shuffle
      create_list = [0] * 64 + [1] * 20 + [2] * 16
      shuffle(create_list)
      # найдем количество обновлений списка
      # добавим один
      try:
         random_object = LuftBallons.objects.order_by('id')[0]
         update_new = random_object.update + 1

      except:
         update_new = 1

      # отчистили таблицу
      LuftBallons.objects.all().delete()
      # создание индекса
      indexes = list(range(1,101))
      # создадим новый список
      objs = list(map(lambda x, y: LuftBallons(id=y, ball=x, update=update_new), create_list, indexes))
      return LuftBallons.objects.bulk_create(objs)
   
   class Meta:
      model = LuftBallons
      fields = ["ball", "id","update"]



class LuftBallonsGuessSerializer(serializers.ModelSerializer):
      choice = serializers.IntegerField(read_only=True)
      
      def validate(self, data):
         obj = LuftBallons.objects.get(id = data["ballon"].id)

         if obj.guessed == True:
            raise serializers.ValidationError({"detail":"you are alredy find color of ballon"})
         
         return data

      
      def create(self, validated_data):
         
         from django.db.models import Q
         
         # считаем, сколько ещё не найдено - n, каждого цвета
         obj_all = LuftBallons.objects.all()
         amount_blue  = obj_all.filter(Q(ball = 0) & Q(guessed=False)).count()
         amount_green = obj_all.filter(Q(ball = 1) & Q(guessed=False)).count()
         amount_red   = obj_all.filter(Q(ball = 2) & Q(guessed=False)).count()

         # считаем, сколько всего осталось неотгадано - m
         amount_guessed = amount_blue + amount_green + amount_red

         # считаем вероятности для каждого цвета
         guess = ((amount_blue/amount_guessed, 0), (amount_green/amount_guessed,1), (amount_red/amount_guessed,2))
         
         # либо создаем, либо обновляем объект
         obj_guess, created = LuftBallonsGuess.objects.update_or_create(**validated_data)

         # находим цвет, который имеет на данный момент наибольшую вероятность
         guessed = max(guess)[1]

         # если он уже существовал, значит не угадали
         # нужно попробовать другой цвет
         if not created:
            if obj_guess.choice == max(guess)[1]:
               guessed = max(guess[1:])[1]
            if obj_guess.choice == max(guess[1:])[1]:
               guessed = min(guess)[1]

         # подставляем, какое предположение мы делаем
         obj_guess.choice = guessed
         
         # сохраняем, чтобы в следующий раз всё было на мази
         # и не пришлось создавать заново элемент
         obj_guess.save()
         

         # получаем соответствующий элемент из шаров
         obj = LuftBallons.objects.get(id = obj_guess.ballon.id)
         # проверяем, угадали ли мы
         if obj.ball == guessed:
            obj.guessed = True
            obj.save()

         return obj_guess
         
      class Meta:
        model = LuftBallonsGuess
        fields = "__all__"
      
from django.db import models

from django.conf import settings

values = (
        (0, 'синий'), 
        (1, 'зеленый'),
        (2, 'красный'),
    )
class LuftBallons(models.Model):
    ball = models.IntegerField(choices = values)
    update = models.IntegerField()
    guessed = models.BooleanField(default=False)
    class Meta:
        verbose_name = ("LuftBallon") # человекочитаемое имя объекта
        verbose_name_plural = ("LuftBallons")  #человекочитаемое множественное 
    def __str__(self):
        return str(self.update)  # __str__ применяется для отображения объекта в интерфейсе

class LuftBallonsGuess(models.Model):
    ballon = models.ForeignKey(LuftBallons, on_delete=models.CASCADE)
    choice = models.IntegerField(null=True)
    class Meta:
        verbose_name = ("Guess") # человекочитаемое имя объекта
        verbose_name_plural = ("Guesses")  #человекочитаемое множественное 
    def __str__(self):
        return str(self.ballon)  # __str__ применяется для отображения объекта в интерфейсе



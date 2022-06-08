from django.db import models

from django.conf import settings

values = (
        (0, 'синий'), 
        (1, 'зеленый'),
        (2, 'красный'),
    )
class LuftBallons(models.Model):
    ball = models.IntegerField(choices = values)
   
    class Meta:
        verbose_name = ("LuftBallon") # человекочитаемое имя объекта
        verbose_name_plural = ("LuftBallons")  #человекочитаемое множественное 
    def __str__(self):
        return self.id  # __str__ применяется для отображения объекта в интерфейсе
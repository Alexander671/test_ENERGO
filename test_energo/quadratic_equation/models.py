from django.db import models

from django.conf import settings


class Equations(models.Model):
    a = models.IntegerField(default=1,blank=True)
    b = models.IntegerField(default=1,blank=True)
    c = models.IntegerField(default=1,blank=True)
    d = models.FloatField(null=True)
    x1 = models.FloatField(null=True)
    x2 = models.FloatField(null=True)
    
    class Meta:
        verbose_name = ("Equation") # человекочитаемое имя объекта
        verbose_name_plural = ("Equations")  #человекочитаемое множественное 
    def __str__(self):
        return self.id  # __str__ применяется для отображения объекта в интерфейсе
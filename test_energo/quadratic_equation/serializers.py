from rest_framework import serializers

from .models import Equations
from math import sqrt


class EquationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    a = serializers.IntegerField()
    b = serializers.IntegerField()
    c = serializers.IntegerField()
    d = serializers.FloatField(read_only=True)
    x1 = serializers.FloatField(read_only=True)
    x2 = serializers.FloatField(read_only=True)

    class Meta:
        model = Equations
        fields = "__all__"
        
    def validate(self, data):
        d = data["b"] ** 2 - (4 * data["a"] * data["c"])
        if d < 0:
            raise serializers.ValidationError({"detail":"negative discriminant"})
        return data

    def create(self, validated_data):
        d,x1,x2 = quadratic(validated_data.get("a", None),
                                          validated_data.get("b", None),
                                          validated_data.get("c", None),)

        return Equations.objects.create(d=d, x1=x1, x2=x2, **validated_data)        
        
def quadratic(a: int, b: int, c: int):
            d = b ** 2 - (4 * a * c)
            if d < 0:
                response = 0,0,0
            elif d == 0:
                x = (- b) / (2 * a)
                response = d, x, x
            else:
                x1 = ((-b) + sqrt(d)) / (2 * a)
                x2 = ((-b) - sqrt(d)) / (2 * a)
                response = d, x1, x2
        
            return response


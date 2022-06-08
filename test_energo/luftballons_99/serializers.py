from rest_framework import serializers

from .models import LuftBallons

class LuftBallonsSerializer(serializers.Serializer):
   id = serializers.IntegerField(read_only=True)
   balls = serializers.IntegerField()
   class Meta:
        model = LuftBallons
        fields = "__all__"
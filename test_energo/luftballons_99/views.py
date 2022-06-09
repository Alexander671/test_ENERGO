from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics

from .models import LuftBallons, LuftBallonsGuess
from .serializers import LuftBallonsGuessSerializer, LuftBallonsListSerializer, LuftBallonsSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
# работа со всеми шариками
class LuftBallonsList(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = LuftBallonsSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    queryset = LuftBallons.objects.all()
    
    # получить
    def get(self, request, format=None):
        ballons = LuftBallons.objects.all()
        serializer = LuftBallonsListSerializer(ballons, many=True)
        return Response(serializer.data)

    # обновить таблицу шаров
    # удаляет предыдущий набор
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# детали по одному шару
class LuftBallonsDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = LuftBallons.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    def get(self, request, pk=None):
        try:
            queryset = LuftBallons.objects.get(id=pk)
        except LuftBallons.DoesNotExist:
            queryset = None
        serializer = LuftBallonsListSerializer(queryset)
        return Response(serializer.data)

# попытки угадать
class LuftBallonsGuess(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = LuftBallonsGuessSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

    queryset = LuftBallonsGuess.objects.all()

    # чтобы знать какие были попытки
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # выбираем элемент
    # внутри прописана логика
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

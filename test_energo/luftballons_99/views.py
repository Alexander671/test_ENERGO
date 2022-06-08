from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LuftBallonsSerializer
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticated

class LuftBallonsList(APIView):
    serializer_class = LuftBallonsSerializer
    permission_classes = [IsAdminUser,  IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, format=None):
        from random import shuffle
        serializer = LuftBallonsSerializer(data=request.data)
        create_list = [0] * 64 + [1] * 20 + [2] * 16
        shuffle(create_list)
        
        if serializer.is_valid():

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
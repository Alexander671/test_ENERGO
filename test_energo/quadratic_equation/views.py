from ast import Eq
from .models import Equations
from .serializers import EquationSerializer
from rest_framework import mixins
from rest_framework import generics

class EquationsList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Equations.objects.all()
    serializer_class = EquationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EquationsDetail(mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Equations.objects.all()
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
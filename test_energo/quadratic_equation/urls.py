from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EquationsDetail, EquationsList

urlpatterns = [
    path('', EquationsList.as_view(), name='equations'),
    path('<int:pk>/', EquationsDetail.as_view(), name='equations_detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
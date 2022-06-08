from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LuftBallonsList

urlpatterns = [
    path('', LuftBallonsList.as_view(), name='luftballons'),


]

urlpatterns = format_suffix_patterns(urlpatterns)
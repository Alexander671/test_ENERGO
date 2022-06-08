from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LuftBallonsDetail, LuftBallonsList, LuftBallonsGuess

urlpatterns = [
    path('', LuftBallonsList.as_view(), name='luftballons'),
    path('<int:pk>/', LuftBallonsDetail.as_view(), name='luftballons_detail'),
    path('guess', LuftBallonsGuess.as_view(), name='guess')


]

urlpatterns = format_suffix_patterns(urlpatterns)
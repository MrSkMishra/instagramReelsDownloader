from django.urls import path
from .views import *


app_name = 'apis'
urlpatterns = [
    path('',download_video,name='api-download'),
    path('remove_background/', RemoveBackgroundView.as_view(), name='remove_background'),
]

from django.urls import path
from .views import create_time, disputa, ranking, index, delete_disputas, delete_times

urlpatterns = [
    path('', index),
    path('time', create_time, name='create_time'),
    path('disputa', disputa, name='disputa'),
    path('ranking', ranking, name='ranking'),
    path('delete_disputas', delete_disputas, name='delete_disputas'),
    path('delete_times', delete_times, name='delete_times'),
]
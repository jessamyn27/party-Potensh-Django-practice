from django.urls import path
from . import views
# this is kind of like our route with a predefined path
urlpatterns=[
    path('', views.artist_list, name='artist_list')
]

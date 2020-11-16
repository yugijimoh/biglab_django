from django.urls import path

from . import entity_rec

urlpatterns = [
    path('',entity_rec.entity_rec , name='entity_rec'),
]
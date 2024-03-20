from django.urls import path
from .views import getNotes, getNote

urlpatterns = [
    path('notes/', getNotes, name='notes'),
    path('note/<str:pk>', getNote, name='note')
]
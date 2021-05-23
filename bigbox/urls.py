from django.urls import path
from . import views

urlpatterns = [
    path('box/', views.box_list, name= 'box_list'),
]
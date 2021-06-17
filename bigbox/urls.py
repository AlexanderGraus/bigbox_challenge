from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.box_list, name= 'box_list'),
    path('<int:pk>/',views.box_detail, name= 'box_detail_pk'),
    path('<str:slug>/', views.box_detail, name= 'box_detail_slug'),
    path('<int:pk>/activity/',views.activity_list_by_box, name= 'activity_list_by_box'),
    path('<int:box_pk>/activity/<int:activity_pk>/', views.activity_detail_by_box, name='activity_detail_by_box')
]
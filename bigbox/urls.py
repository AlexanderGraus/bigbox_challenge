from django.urls import path
from . import views

urlpatterns = [
    path('box/', views.box_list, name= 'box_list'),
    path('box/<int:pk>/',views.box_detail, name= 'box_detail'),
    path('box/<int:pk>/activity/',views.activity_list_by_box, name= 'activity_list_by_box'),
    path('box/<int:box_pk>/activity/<int:activity_pk>/', views.activity_detail_by_box, name='activity_detail_by_box')
]
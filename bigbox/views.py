from django.shortcuts import render
from .models import Box, Activity, Category, Reason

# Create your views here.

def box_list(request):
    boxes = Box.objects.all()
    return render(request,'box_list.html',{'boxes':boxes})
from django.shortcuts import render
from .models import Box, Activity, Category, Reason
from django.shortcuts import get_object_or_404
# Create your views here.

def box_list(request):
    boxes = Box.objects.all()
    return render(request,'box_list.html',{'boxes':boxes})

def box_detail(request,pk):
    box = Box.objects.get(pk=pk)
    activities = box.activities.all()[:5] # guarda las primeras 5 activities
    return render(request,'box_detail.html',{"box":box,"activities":activities})

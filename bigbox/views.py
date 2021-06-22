from django.shortcuts import render, redirect
from .models import Box, Activity
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

# Create your views here.

def box_list(request):
    boxes = Box.objects.all()
    return render(request,'box_list.html',{'boxes':boxes})

def box_detail(request,pk=None,slug=None): # como no se si el user va a buscar por pk o por slug, el valor por defecto de ambos es None
    if pk:
        box = Box.objects.get(pk=pk)
    else:
        box = Box.objects.get(slug=slug)
    activities = box.activities.all()[:5] # guarda las primeras 5 activities
    return render(request,'box_detail.html',{"box":box,"activities":activities})

def activity_list_by_box(request,pk):
    activities = Activity.objects.filter(box__pk=pk)
    box = Box.objects.get(pk=pk)

    paginator = Paginator(activities, settings.PAGINADOR_ACTIVITY) 
    page = request.GET.get('page')
    activities = paginator.get_page(page)
    return render(request,'activity_list.html',{"box":box, "activities":activities})

def activity_detail_by_box(request,box_pk,activity_pk):
    activity = Activity.objects.get(pk=activity_pk, box__pk=box_pk) # devuelve la activity buscada si coincide con el box id
    box = Box.objects.get(pk= box_pk)
    return render(request,'activity_box_detail.html',{"box":box, "activity":activity})

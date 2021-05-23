from django.shortcuts import render
from .models import Box, Activity, Category, Reason
from django.core.paginator import Paginator
# Create your views here.

def box_list(request):
    boxes = Box.objects.all()
    return render(request,'box_list.html',{'boxes':boxes})

def box_detail(request,pk):
    box = Box.objects.get(pk=pk)
    activities = box.activities.all()[:5] # guarda las primeras 5 activities
    return render(request,'box_detail.html',{"box":box,"activities":activities})

def activity_list_by_box(request,pk):
    box_name = Box.objects.get(pk=pk).name
    activities = Activity.objects.filter(box__pk=pk)
    print(activities[0].name)
    print(box_name)

    paginator = Paginator(activities, 20) # muestra 20 resultados por pagina
    page = request.GET.get('page')
    activities = paginator.get_page(page)
    return render(request,'activity_list.html',{"activities":activities, "box_name":box_name})
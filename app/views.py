from django.shortcuts import render, redirect
from . models import *

def show(request) : 
    context={
        "title": "Shows",
        "shows": Show.objects.all(),
    }
    
    return render (request, "shows.html", context)

def newshowform(request):    
    context={
        "title": "Add a Show",
    }
    # return redirect("/shows/new/")
    return render (request, "newshow.html", context)

def addshow(request):
    # print(request.POST) Se usa para VERIFICAR !!!
    show=Show.objects.create(
        title=request.POST['show_title'], 
        network=request.POST['show_network'], 
        date=request.POST['rdate'], 
        desc=request.POST['show_desc'],)
    
    return redirect("/shows")

def detail(request,num):
    context={
        "show": Show.objects.get(id=num),
    }  
    return render (request, "detail.html", context)

# def detail(request, num):
#     show=Show.objects.delete(id)
    
#     return render (request, "detail.html", context)
    
def destroy(request,num):
    show = Show.objects.get(id=num)
    show.delete() 
    return redirect("/shows")

def editshow(request,num):
    print(request.POST)
    show = Show.objects.get(id=num)
    show.title = request.POST['show_title']
    show.network = request.POST['show_network']
    show.date=request.POST['rdate'] 
    show.desc=request.POST['show_desc']
    show.save()
    return redirect(f"/shows/{show.id}")

def edit(request,num):
    context={
        "show": Show.objects.get(id=num),
    }  
    return render (request, "edit.html", context)



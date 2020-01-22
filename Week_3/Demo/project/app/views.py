from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "shows":Show.objects.all()
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    errors = Show.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/show/new')

    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
    return redirect('/shows')

def show_one(request, id):
    one_show = Show.objects.filter(id = id).first()
    if one_show:
        context = {
            "show":one_show
        }
        return render(request, 'one_show.html', context)
    else:
        return redirect('/shows')

def delete(request, id):
    one_show = Show.objects.filter(id = id).first()
    if one_show:
        one_show.delete()
    return redirect('/shows')

def edit(request, id):
    one_show = Show.objects.filter(id = id).first()
    if one_show:
        context = {
            "show": one_show
        }
        return render(request, 'edit.html', context)
    return redirect('/shows')

def update(request, id):
    errors = Show.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/show/{id}/edit')

    does_exist = Show.objects.filter(title=request.POST['title']).first()
    if does_exist:
        messages.error(request, "Title needs to be unique")
        return redirect(f'/show/{id}/edit')
    
    one_show = Show.objects.filter(id = id).first()

    one_show.title = request.POST['title']
    one_show.network = request.POST['network']
    one_show.description = request.POST['description']
    one_show.release_date = request.POST['release_date']
    one_show.save()
    return redirect(f'/show/{id}')
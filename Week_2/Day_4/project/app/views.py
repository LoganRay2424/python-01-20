from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    all_people = Person.objects.all()
    context = {
        "ppl":all_people
    }
    return render(request, 'index.html', context)

def new_person(request):
    Person.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect('/')

def new_gift(request):
    person_gifted = Person.objects.get(id = request.POST['person'])
    Gift.objects.create(gift = request.POST['gift'], user_who_got_gift = person_gifted)
    return redirect('/')
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    user_in_db = User.objects.filter(email = request.POST['email']).first()

    if user_in_db:
        messages.error(request, "Invalid cradentials")
        return redirect('/')
    
    hashed_password = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(
        first_name= request.POST['fname'],
        last_name = request.POST['lname'],
        email = request.POST['email'],
        password = hashed_password
    )

    request.session['user_id'] = new_user.id

    return redirect('/success')

def success(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.error(request, "Please log in or register")
        return redirect('/')

    context = {
        "user":User.objects.get(id=user_id),
        "good_dog": Dog.objects.filter(is_good_boy=True),
        "bad_dog":Dog.objects.filter(is_good_boy=False)
    }
    return render(request, 'success.html', context)

def login(request):
    found_user = User.objects.filter(email = request.POST['email'])
    if len(found_user)>0:
        user_from_db = found_user[0]
        
        is_pw_correct = bcrypt.checkpw(
            request.POST['password'].encode(),
            user_from_db.password.encode()
        )
        if is_pw_correct:
            request.session['user_id'] = user_from_db.id
            return redirect('/success')
    messages.error(request, "Invalid cradentials")
    return redirect('/')

def new_dog(request):
    all_tricks = Trick.objects.all()
    context = {
        "tricks":all_tricks
    }
    return render(request, 'new_dog.html', context)

def create_dog(request):
    user_id = request.session.get('user_id')

    if user_id is None:
        return redirect("/")

    errors = Dog.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dog/new')
    
    user_submitted = User.objects.get(id=user_id)

    new_dog = Dog.objects.create(
        name= request.POST['name'],
        profile_pic_url = request.POST['profile_pic'],
        bio = request.POST['bio'],
        age = request.POST['age'],
        birthday = request.POST['bday'],
        weight = request.POST['weight'],
        submitted_by = user_submitted
    )

    checkbox = request.POST.getlist('trick')
    print(checkbox)
    if checkbox is not None:
        for trick in checkbox:
            trick_from_db = Trick.objects.get(id=trick)
            new_dog.tricks.add(trick_from_db)

    other_trick = request.POST['other']

    if other_trick!="":
        current = other_trick.lower().capitalize()
        trick_from_db = Trick.objects.filter(name=current)
        if len(trick_from_db)==0:
            new_trick = Trick.objects.create(name=current)
            new_dog.tricks.add(new_trick)
    return redirect('/success')

def toggle(request, id):
    user_id = request.session.get('user_id')

    if user_id is None:
        return redirect("/")

    dog_from_db = Dog.objects.get(id=id)
    if dog_from_db is not None:
        dog_from_db.is_good_boy = not dog_from_db.is_good_boy
        dog_from_db.save()
    
    return redirect('/success')

def one_dog(request, id):
    user_id = request.session.get('user_id')

    if user_id is None:
        return redirect("/")

    dog_from_db = Dog.objects.get(id=id)

    context = {
        "dog": dog_from_db
    }

    return render(request, 'one_dog.html', context)

def edit_dog(request, id):
    user_id = request.session.get('user_id')

    if user_id is None:
        return redirect("/")

    dog_from_db = Dog.objects.get(id=id)

    context = {
        "dog": dog_from_db
    }

    return render(request, 'edit.html', context)

def update_dog(request, id):
    user_id = request.session.get('user_id')

    if user_id is None:
        return redirect("/")

    errors = Dog.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/dog/{id}/edit')

    dog_from_db = Dog.objects.get(id=id)

    dog_from_db.name = request.POST['name']
    dog_from_db.profile_pic_url = request.POST['profile_pic']
    dog_from_db.bio = request.POST['bio']
    dog_from_db.age = request.POST['age']
    dog_from_db.weight = request.POST['weight']
    dog_from_db.birthday = request.POST['bday']
    dog_from_db.save()

    return redirect(f'/dog/{id}')

def delete(request, id):
    user_id = request.session.get('user_id')

    if user_id is None:
        return redirect("/")
    
    dog_from_db = Dog.objects.get(id=id)
    dog_from_db.delete()
    return redirect('/success')
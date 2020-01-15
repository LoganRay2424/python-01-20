from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, 'index.html')

def login(request):
    user_from_db = User.objects.filter(email = request.POST['email']).first()

    if user_from_db is None:
        print("User not found")
    else:
        if user_from_db.password == request.POST['password']:
            request.session['user_id'] = user_from_db.id
            return redirect('/success')
        else:
            print("password incorrect!")
    return redirect('/')

def success(request):
    user_logged_in = User.objects.get(id = request.session['user_id'])
    if user_logged_in is None:
        return redirect('')
    context = {
        "user":user_logged_in
    }
    return render(request, 'success.html', context)
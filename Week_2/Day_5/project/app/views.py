from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def submit(request):
    errors = User.objects.validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        create_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password = request.POST['password'], birth_day=request.POST['bday'], bio=request.POST['bio'])
        request.session['user_id'] = create_user.id
        return redirect('/success')

def success(request):
    user_id = request.session.get('user_id')

    if user_id is None:
        messages.error(request, 'Try to login/register')
        return redirect('/')
    else:
        context = {
            "user":User.objects.get(id=user_id)
        }
        return render(request, 'success.html', context)
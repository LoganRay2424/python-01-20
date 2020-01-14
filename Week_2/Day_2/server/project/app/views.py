from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_password(request):
    request.session['length'] = request.POST['pass_length']
    print('*'*100)
    print(request.session['length'])
    return redirect('/success')

def show_password(request):
    unique_string = get_random_string(length = int(request.session['length']))
    context = {
        "rand_string": unique_string
    }
    return render(request, 'success.html', context)

def restart(request):
    request.session.clear()
    return redirect('/')
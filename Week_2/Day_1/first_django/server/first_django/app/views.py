from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def new_page(request):
    context = {
        "cute_animals" : ["cat", "penguin", "dog", "bunny", "chinchilla", "koala"]
    }
    return render(request, 'abc.html', context)

def form_sub(request):
    print('*'*100)
    print(request.POST)
    print(request.POST['password'])
    return redirect('/')
from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index), #GET
    path('register', views.register), #POST
    path('success', views.success), #GET
    path('logout', views.logout), #GET
    path('login', views.login), #POST
    path('dog/new', views.new_dog), #GET
    path('dog/create', views.create_dog), #POST
    path('dog/<int:id>/toggle', views.toggle), #GET
    path('dog/<int:id>', views.one_dog), #GET
    path('dog/<int:id>/edit', views.edit_dog), #GET
    path('dog/<int:id>/update', views.update_dog), #POST
    path('dog/<int:id>/delete', views.delete) #GET
]
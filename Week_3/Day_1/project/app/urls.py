from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index), #GET
    path('register', views.register), #POST
    path('success', views.success), #GET
    path('logout', views.logout), #GET
    path('login', views.login), #POST
]
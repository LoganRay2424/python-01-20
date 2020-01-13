from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index),
    path('abc', views.new_page),
    path('new', views.form_sub)
]
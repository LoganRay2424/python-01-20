from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('newPerson', views.new_person),
    path('newGift', views.new_gift)
]
from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('passLength', views.create_password),
    path('success', views.show_password),
    path('restart', views.restart)
]
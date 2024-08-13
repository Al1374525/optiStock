from django.urls import path, include
from .views import home

app_name = 'stocks'
urlpatterns = [
    path('', home, name='home'),
]


from django.urls import path
from . import views

app_name= 'generator'

urlpatterns = [
    path('', views.generator, name='generatePage'),
    path('password', views.password, name='passPage')
]
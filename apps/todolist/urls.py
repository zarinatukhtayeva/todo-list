from django.urls import path
from apps.todolist import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home')
]
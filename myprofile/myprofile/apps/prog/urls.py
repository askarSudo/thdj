from django.urls import path

from . import views

app_name = 'prog'
urlpatterns = [
    path('', views.Program_def , name = 'Program_def'),

]
from django.urls import path

from . import views

app_name = 'audio'
urlpatterns = [
    path('', views.index , name = 'index'),

]
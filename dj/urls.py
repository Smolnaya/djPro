from . import views
from django.urls import path


app_name = 'dj'

urlpatterns = [
    path('', views.index, name='index'),
    path('students', views.showStudents, name='students'),
    path('api/get', views.getJson, name='api/get')
]

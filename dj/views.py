from django.http import HttpResponse
from django.shortcuts import render
from dj.models import *
from django.core import serializers


def index(request):
    return HttpResponse('Try: .../students\n or \n.../api/get')


def showStudents(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)


def getJson(request):
    return HttpResponse(serializers.serialize("json", Student.objects.all(),
                                              fields=('stSurname', 'stMark')))

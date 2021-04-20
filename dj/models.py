from django.db import models


class Student(models.Model):
    stName = models.fields.CharField(max_length=50)
    stSurname = models.fields.CharField(max_length=50)
    stSubject = models.fields.CharField(max_length=50, default='Human-Oriented Interface Design')
    stMark = models.fields.IntegerField()

    def __str__(self):
        return f'{self.stName} {self.stSurname}'

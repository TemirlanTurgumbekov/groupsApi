from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contacts = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Group(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, related_name='groups')

    def __str__(self):
        return self.title
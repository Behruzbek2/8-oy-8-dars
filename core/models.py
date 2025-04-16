from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=31)
    surname = models.CharField(max_length=31)

    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=31)
    surname = models.CharField(max_length=31)

    classes = models.ManyToManyField(Class)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    time = models.DateTimeField(auto_now_add=True)

    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name= "schedule")
    clas = models.ForeignKey(Class, on_delete=models.DO_NOTHING, related_name= "schedule")
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, related_name= "schedule")

    def __str__(self):
        return f"{self.time}, {self.subject}, {self.clas}, {self.teacher}"
    
class Grade(models.Model):
    grade = models.IntegerField()

    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, related_name= "grade")
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING, related_name= "schedule")

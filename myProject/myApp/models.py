from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):
    gender=(
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(choices = gender, blank = True, max_length= 20)
    def __str__(self):
        return self.first_name





class Subject_Model(models.Model):
    subject_title = models.CharField(max_length = 100)
    subject_code = models.IntegerField()
    subject_credit = models.IntegerField()
    def __str__(self):
        return self.subject_title
    

class Student_Model(models.Model):
    student_name = models.CharField(max_length = 100)
    student_roll = models.IntegerField()
    student_department = models.CharField(max_length = 100)
    subject = models.ManyToManyField(Subject_Model, blank = True)
    
    create_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.student_name
    
    
class Grade_Model(models.Model):
    student_model = models.ForeignKey(Student_Model, on_delete = models.CASCADE)
    subject_model = models.ForeignKey(Subject_Model, on_delete = models.CASCADE)
    marks = models.FloatField()
    cgpa = models.FloatField(null = True)
    create_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.student_model.student_name
    
class Result_Model(models.Model):
    student = models.ForeignKey(Student_Model , on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject_Model , on_delete= models.CASCADE)
    gread = models.ForeignKey(Grade_Model , on_delete= models.CASCADE)
    def __str__(self):
        return self.student.student_name


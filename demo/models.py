from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name= models.CharField(max_length=25,unique=True)
    address=models.CharField(max_length=50)

# class Subject(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(unique=False)
#     stu_id = models.ForeignKey(Student,on_delete=models.CASCADE)
#     time_of_period = models.DateTimeField
#     teachers = models.ManyToManyField(
#         Subject,
#         through='SubjectTeacher',
#         related_name='teachers'
#     )
    

    
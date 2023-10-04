from django.db import models

# Create your models here.
class CourseModel(models.Model):
    Course_Name=models.CharField(max_length=70)
    Course_Fees=models.CharField(max_length=70)

    # def __str__(self):
    #     return self.Course_Name

class StudentModel(models.Model):
    Course=models.ForeignKey(CourseModel,on_delete=models.CASCADE,null=True)
    Std_Name=models.CharField(max_length=100)
    Std_Address=models.IntegerField()
    Std_Age=models.IntegerField()
    

    # def __str__(self):
    #     return self.Std_Name
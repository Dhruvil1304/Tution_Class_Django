from django.db import models

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=30)
    duration=models.CharField(max_length=20)
    description=models.TextField()
    fees=models.IntegerField()


    def __str__(self):
        return f"course(Course_name={self.course_name},duration={self.duration},fees={self.fees})"
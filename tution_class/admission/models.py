from django.db import models
from tution_class.students.models import students
from tution_class.course.models import course
# Create your models here.
class admission(models.Model):
    student_id=models.ForeignKey(students,on_delete=models.CASCADE,blank=True)
    course_id=models.ForeignKey(course,on_delete=models.CASCADE,blank=True)
    date_of_joining=models.DateField()
    date_of_certification=models.DateField()

    def __str__(self):
        return f"student_id{self.student_id},course_id{self.course_id},date_of_joining{self.date_of_joining},date_of_certification{self.date_of_certification}"

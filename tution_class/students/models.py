from django.db import models

# Create your models here.
class students(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    local_address=models.TextField()
    area=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=10)
    clg=models.CharField(max_length=30)
    sem=models.IntegerField()
    Id_type=models.CharField(max_length=20)


    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.phone_no}"




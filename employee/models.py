from django.db import models

# Create your models here.
class A_data(models.Model):
    certi_no = models.CharField(max_length = 255, default=False)
    username = models.CharField(max_length = 255)
    course = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.certi_no

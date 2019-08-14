from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Photo(models.Model):
    File_name= models.CharField(max_length=100)
    photos= models.ImageField(upload_to='images', null=True, blank=True)

def __str__(self):
    return self.File_name





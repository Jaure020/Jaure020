from django.db import models

# Photo Class which contains the file name and image
class Photo(models.Model):
    File_name= models.CharField(max_length=100)
    photos= models.ImageField(upload_to='images', null=True, blank=True)

def __str__(self):
    return self.File_name





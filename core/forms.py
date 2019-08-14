from django import forms
from .models import Photo

#Form for uploading photo image
class PhotoForm(forms.ModelForm):
    class Meta:
        model= Photo
        fields= ('File_name', 'photos')
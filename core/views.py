from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
import requests
from .forms import PhotoForm
from .models import Photo

#Class for sign_up form including form, redirection of urls, and html templates
class Sign_up(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#Class for photo_form including form, redirection of urls, and html templates
class Photo_form(generic.CreateView):
    form_class = PhotoForm
    success_url = reverse_lazy('ecSeg')
    template_name = 'ecSeg.html'


#Class for home including forms, redirection of urls, and html templates
class home(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home/')
    template_name = 'home.html'

#Logout redirect
def logout_view(request):
    logout(request)

# Future ecSeg script for calling server that runs ecSeg
def output(request):
    data = requests.get("https://www.heroku.com/")
    print(data.text)
    data = data.text
    return render(request, 'ecSeg.html', {'data': data})

#File upload
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        return render(request, 'display_photos.html')
        context['url'] = fs.url(name)
    return render(request, 'display_photos.html', context)

#Displays photos
def display_photos(request):
    photos = Photo.objects.all()
    return render(request, 'display_photos.html', {
        'photos': photos
    })

#Connected to upload and uploads photos
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_photos')
    else:
        form = PhotoForm()
    return render(request, 'display_photos.html', {
        'form': form
    })

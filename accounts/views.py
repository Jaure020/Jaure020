from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
import requests
from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ecSeg(generic.CreateView):
    form_class = PhotoForm
    success_url = reverse_lazy('ecSeg')
    template_name = 'ecSeg.html'


class home(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home/')
    template_name = 'home.html'


def logout_view(request):
    logout(request)


def output(request):
    data = requests.get("https://www.heroku.com/")
    print(data.text)
    data = data.text
    return render(request, 'ecSeg.html', {'data': data})


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        return render(request, 'upload.html')
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def display_photos(request):
    photos = Photo.objects.all()
    return render(request, 'display_photos.html', {
        'photos': photos
    })


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_photos')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {
        'form': form
    })
# def test1(request):
#     return render(request, "display_photos.html")

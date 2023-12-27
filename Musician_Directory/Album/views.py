from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')

    else:
        album_form = forms.AlbumForm()
    return render(request, 'album.html', {'form': album_form})



def edit_album(request, id):
    album = models.AlbumModel.objects.get(pk=id)
 
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
          
 
    else:
        album_form = forms.AlbumForm(instance=album)
 
    return render(request, 'album.html', {'form': album_form})


def delete_album(request, id):
    album = models.AlbumModel.objects.get(pk=id)  
    album.delete()
    return redirect('homepage')

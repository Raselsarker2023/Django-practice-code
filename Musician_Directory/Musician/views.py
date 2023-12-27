from django.shortcuts import render
from . import forms

# Create your views here.
def add_musician (request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            request.redirect('add_musician')
            
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'musician.html', {'form':musician_form})
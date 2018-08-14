from django.shortcuts import render

# Create your views here.
# this is where we are doing our 'route' or controller
from .models import Artist
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'practice/artist_list.html' , {'artists': artists})

    # first we grab all Artists found in the db and storing it in a new variable called artists
    # then we are asking to render ths file 'practice/artist_list.html' ontu the server in this case the values that get passed to the template is the object artists

from django.shortcuts import render_to_response
from Main.models import Artist, Genre, Song

def index(request):
    latest_song_list = Song.objects.all().order_by('-pub_date')[:5]
    return render_to_response('index.html', {'latest_poll_list': latest_song_list})
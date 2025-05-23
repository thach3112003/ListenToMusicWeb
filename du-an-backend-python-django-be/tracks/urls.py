# users/urls.py
from django.urls import path, include
from .views import *
urlpatterns = [
    path('create/', CreateTrackView.as_view(), name='register'),
    path('update/<int:track_id>/', UpdateTrackView.as_view(), name='update-track'),
    path('delete/<int:track_id>/', DeleteTrackView.as_view(), name='delete-track'),
    path('getbyalbum/<int:album_id>/', GetTrackbyAlbums, name='tracks-by-albums'),
    path('getbyartist/<int:artist_id>/', GetTrackbyArtist, name='tracks-by-artist'),
    path('list/', ListTrackView.as_view(), name='tracks-by-artist'),
    path('toptrack/', ListTrackTopView.as_view(), name='all_tracks'),
    path('top10track/', Top10TrackView.as_view(), name='top10_tracks'),
    path('artist-top/<int:artist_id>/', TracksByArtistView.as_view(), name='tracks_by_artist'),
    path('search-by-artist/', search_by_artist, name='search_by_artist'),
    path('search/',search_track, name='search_track')

]
#hung ngáo
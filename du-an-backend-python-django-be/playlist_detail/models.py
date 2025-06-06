from django.db import models
from tracks.models import Tracks
from playlists.models import Playlists

class Playlists_Detail(models.Model):
    playlist_id = models.ForeignKey(Playlists, on_delete=models.CASCADE, db_column='playlist_id')
    track_id = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column='track_id')

    class Meta:
        managed = False
        db_table = 'playlists_detail'
        unique_together = (('playlist_id', 'track_id'),)

from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from albums.models import Albums
from artists.models import Artists
class Tracks(models.Model):
    track_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Albums, models.DO_NOTHING, blank=True, null=True)
    artist = models.ForeignKey(Artists, models.DO_NOTHING, blank=True, null=True)
    is_copyright = models.IntegerField(db_column='is_Copyright', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    namemp3 = models.CharField(max_length=200)
    class Meta:
        managed = False
        db_table = 'tracks'
>>>>>>> bcd161744d1fcd440b67199d4c12899411df4d0d

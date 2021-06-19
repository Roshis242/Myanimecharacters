from django.db import models

# Create your models here.
class Animecharacter(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alias_name = models.CharField(max_length=200)
    anime_name = models.CharField(max_length=200)
    anime_seasons = models.IntegerField()
    role_in_anime = models.CharField(max_length=200)
    desc = models.TextField()
    photo = models.FileField()

    def __str__(self):
        return self.first_name

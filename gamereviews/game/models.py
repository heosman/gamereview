from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    gamename = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.gamename
 
    class Meta:
        db_table='game'
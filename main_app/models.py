from django.db import models

# Create your models here.
class Die(models.Model):
    sides = models.IntegerField()
    material = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    text_color = models.CharField(max_length=20)

    def __str__(self):
        return self.text_color
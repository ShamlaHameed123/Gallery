from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=150)
    location = models.ImageField()
    rate = models.IntegerField(default=1, validators=[MaxValueValidator(5),
                               MinValueValidator(1)])

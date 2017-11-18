from decimal import Decimal

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=150)
    location = models.ImageField()
    url = models.CharField(max_length=150)
    rate = models.DecimalField(max_digits=3, decimal_places=1,
                               default=Decimal('0.0'))
    score = models.DecimalField(max_digits=3, decimal_places=2,
                                default=Decimal('0.0'))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.url = self.location.url
        super(Photo, self).save(*args, **kwargs)


class RatePhoto(models.Model):
    '''
    Rate a broadcast class
    '''
    photo = models.ForeignKey(Photo)
    rate = models.IntegerField(default=0)

import os
import math

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Avg

from main.utils import make_tree
from main.models import Photo, RatePhoto


def dirtree(request):
    tree = make_tree(settings.MEDIA_ROOT)
    data = {
         'tree': tree,
         'path': settings.MEDIA_ROOT
        }
    return render(request, 'dirtree.html', data)


def delete_fe(request):
    tree = make_tree(settings.MEDIA_ROOT)
    data = {
         'tree': tree,
         'path': settings.MEDIA_ROOT
        }
    return render(request, 'delete_files.html', data)


def delete_photo(request):
    delete_post_url = str(request.POST['delete'])
    delete_url = delete_post_url.split(":")[1]
    Photo.objects.get(url=delete_url).delete()
    os.remove(settings.MEDIA_ROOT+delete_url[6:])
    return HttpResponseRedirect('/delete/')



def rate_photo(request):
    rate_id = request.POST["rate"]
    file_path = str(rate_id.split(":")[0])
    rate_value = rate_id.split(":")[1]
    print file_path, rate_value
    try:
        photo = Photo.objects.get(url=file_path)
        rate = RatePhoto(photo=photo)
        rate.rate = rate_value
        rate.save()
        ratings = RatePhoto.objects.filter(photo=photo)
        photo_rate = ratings.aggregate(Avg('rate'))
        photo_rate_count = ratings.count()
        photo.rate = photo_rate['rate__avg']
        score = float(photo.rate) + 5 *\
	    (1 - math.exp(-photo_rate_count / settings.RATING_PREFERENCE))
        photo.score = score
        photo.save()
    except Photo.DoesNotExist:
        pass
    return HttpResponseRedirect('/gallery/')

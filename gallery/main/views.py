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


def score_board(request):
    photos = Photo.objects.all().order_by('-rate')
    filters = ['<','>','='] 
    data = {
          'photos': photos,
          'filters': filters
    	 }
    return render(request, 'rating_board.html', data)

def filter_result(request):
    filters = str(request.POST['filters'])
    offset = request.POST['offset']
    if filters == '>':
        photos = Photo.objects.filter(rate__gt=offset)
    elif filters == '<':
        photos = Photo.objects.filter(rate__lt=offset)
    elif filters == '=':
        photos = Photo.objects.filter(rate=offset)
    filters = ['<','>','='] 
    data = {
          'photos': photos,
          'filters': filters
    	 }
    return render(request, 'rating_board.html', data)    


def rate_photo(request):
    rate_id = request.POST["rate"]
    file_path = str(rate_id.split(":")[0])
    rate_value = rate_id.split(":")[1]
    try:
        photo = Photo.objects.get(url=file_path)
        rate = RatePhoto(photo=photo)
        rate.rate = rate_value
        rate.save()
        ratings = RatePhoto.objects.filter(photo=photo)
        photo_rate = ratings.aggregate(Avg('rate'))
        photo_rate_count = ratings.count()
        photo.rate = photo_rate['rate__avg']
        photo.save()
    except Photo.DoesNotExist:
        pass
    return HttpResponseRedirect('/gallery/')

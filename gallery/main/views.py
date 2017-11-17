import os

from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from main.utils import make_tree


def dirtree(request):
    tree = make_tree(settings.MEDIA_ROOT)
    data = {
         'tree': tree,
         'path': settings.MEDIA_ROOT
        }
    return render(request, 'dirtree.html', data)


def delete_photo(request):
    print "delete" + path


def rate_photo(request):
    value = request.POST.get("rate")
    return HttpResponse(value)

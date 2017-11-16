import os

from django.shortcuts import render
from django.conf import settings

from main.utils import make_tree


def dirtree(request):
    tree = make_tree(settings.MEDIA_ROOT)
    data = {
         'tree': tree,
         'path': settings.MEDIA_ROOT
        }
    return render(request, 'dirtree.html', data)

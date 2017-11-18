import os
from django.conf import settings
from main.models import Photo
rootDir = settings.MEDIA_ROOT

for dir_, _, files in os.walk(rootDir):
    for fileName in files:
        relDir = os.path.relpath(dir_, rootDir)
        relFile = os.path.join(relDir, fileName)
        name = relFile.split("/")[1]
        photo = Photo(title=name, location=relFile)
        photo.save()

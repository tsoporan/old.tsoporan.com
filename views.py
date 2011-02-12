from django.http import HttpResponse
from django.conf import settings
import os

ROBOT_FILE_PATH = os.path.join(settings.MEDIA_ROOT, 'robots.txt')

def robots(request):
    return HttpResponse(open(ROBOT_FILE_PATH).read(), 'text/plain')

from django.conf.urls import url
from . import views

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from bps.views import *

urlpatterns = [
    # VFinding VADDfinding VEditFinding
    url(r'^', Main.as_view(), name='index'),
    
]

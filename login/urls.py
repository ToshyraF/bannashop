from django.conf.urls import url
from . import views

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from login.views import *

urlpatterns = [
    # VFinding VADDfinding VEditFinding
    url(r'^order', OrderPage.as_view(), name='index'),
    url(r'^shop', ShopPage.as_view(), name='index'),
    url(r'^province', ProvincePage.as_view(), name='index'),
    url(r'^setting', SettingPage.as_view(), name='index'),
    url(r'^', RegionPage.as_view(), name='index'),
    
]

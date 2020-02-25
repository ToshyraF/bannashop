from django.shortcuts import render
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class LoginPage(ListView):
    @csrf_exempt
    def get(self, request):

        return render(request, 'province.html')
    def post(self, request):
        print('bank')

class OrderPage(ListView):
    @csrf_exempt
    def get(self, request):

        return render(request, 'order.html')


class RegionPage(ListView):
    @csrf_exempt
    def get(self, request):

        return render(request, 'subpage/region.html')

class ProvincePage(ListView):
    @csrf_exempt
    def get(self, request):

        return render(request, 'subpage/province.html')

class ShopPage(ListView):
    @csrf_exempt
    def get(self, request):

        return render(request, 'subpage/shop.html')

class SettingPage(ListView):
    @csrf_exempt
    def get(self, request):

        return render(request, 'setting.html')
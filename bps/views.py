from django.shortcuts import render
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class Main(ListView):
    @csrf_exempt
    def get(self, request):
        return render(request, 'BPS/main.html')
    def post(self, request):
        print('bank')


class Service(ListView):
    @csrf_exempt
    def get(self, request):
        return render(request, 'BPS/service.html')
    def post(self, request):
        print('bank')
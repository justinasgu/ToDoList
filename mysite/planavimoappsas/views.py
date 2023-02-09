from django.shortcuts import render
from django.http import HttpResponse
from .models import Uzduotis
# Create your views here.

def index(request):
    num_uzduotis = Uzduotis.objects.all().count()
    context = {
        'num_uzduotis': num_uzduotis,
    }
    return render(request, 'index.html', context=context)


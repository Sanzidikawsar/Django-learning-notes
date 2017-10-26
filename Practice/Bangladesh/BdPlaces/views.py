from django.shortcuts import render
from django.shortcuts import render
from .models import Place
from .models import SubPlace

# Create your views here.
def home(request):
    all_divisions = Place.objects.all()
    return render(request, 'index.html', {'divisions': all_divisions})


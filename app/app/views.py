from django.http import HttpResponse
from django.shortcuts import render

from .forms import Contactform

def index(request):
    contact_form = Contactform()
    return render(request, 'app/index.html', {'contact_form': contact_form})

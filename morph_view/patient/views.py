from django.shortcuts import render
from .models import *
from morph_view.settings import *


# Create your views here.
def patient_index(request):
    context = {"media": STATIC_URL}
    return render(request, 'patient/patient.html', context=context)

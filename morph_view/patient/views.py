from django.shortcuts import render
from .models import *
from morph_view.settings import *


# Create your views here.
def patient_index(request):

    return render(request, 'patient/patient.html')

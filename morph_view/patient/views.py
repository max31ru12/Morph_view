from django.shortcuts import render


# Create your views here.
def patient_index(request):
    return render(request, 'patient/patient.html')

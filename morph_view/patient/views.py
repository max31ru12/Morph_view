from django.shortcuts import render


# Create your views here.
def patinet_index(request):
    return render(request, 'patient/base.html')

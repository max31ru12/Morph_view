from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from morph_view.settings import *


class PatientPage(ListView):
    model = MainPageVideo
    template_name = 'patient/patient.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {'video': self.model.objects.all()}
        return context



# # Create your views here.
# def show_video(request):
#     video = MainPageVideo.objects.all()
#     return render(request, 'patient/patient.html', {'video': video})

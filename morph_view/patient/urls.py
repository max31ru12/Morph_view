from django.urls import path
from .views import *

urlpatterns = [
    path('', patient_index, name='patient-main-page')
]

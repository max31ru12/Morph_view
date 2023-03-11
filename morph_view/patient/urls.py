from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientPage.as_view(), name='patient-main-page')
]

from django.urls import path
from .views import *

urlpatterns = [
    path('', patinet_index, name='patient-main-page')
]
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, TemplateView
from utils import MainPageMixin

# Create your views here.


# Статическая страница, она не имеет ничего особенного
class MainPage(MainPageMixin, TemplateView):
    template_name = 'mainapp/base.html'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(c_def.items()) + list(context.items()))





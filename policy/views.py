from django.shortcuts import render

from django.conf import settings
from django.views.generic.base import TemplateView



class PolicyPageView(TemplateView):
    template_name = 'policy.html'

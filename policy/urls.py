from django.urls import path

from . import views

urlpatterns = [
    path('', views.PolicyPageView.as_view(), name='policy'),
]
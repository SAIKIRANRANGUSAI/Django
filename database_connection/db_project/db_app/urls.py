from django.urls import path
from . import views

urlpatterns = [
    path('',views.sai, name='sai')
]
from . import views
from django.urls import path
from new.views import welcome

urlpatterns = [
    path('',welcome,name='main'),
]
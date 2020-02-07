from . import views
from django.urls import path


app_name = 'we'

urlpatterns = [
    path('', views.we, name='we'),
    ]


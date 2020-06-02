from django.urls import path
from .views import *

urlpatterns = [
    path('list/', views.index, name = 'list-students'),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('device/', listview.as_view(), name='device-list'),
    path('addname/', addname.as_view(), name='add-name'),



]
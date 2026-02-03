from django.urls import path
from .views import *


urlpatterns = [
    path('device/', listview.as_view(), name='device-list'),
    path('addname/', addname.as_view(), name='add-name'),
    path("device/<int:id>/",DeviceDetailsUpdateDeleteView.as_view(),name="device-update-delete"),



]
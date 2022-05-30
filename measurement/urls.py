from django.urls import path

from measurement.views import SensorView, MeasurementView, OneSensorView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('temps/', MeasurementView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
]

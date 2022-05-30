# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        return Response({'status': 'OK_sensor'})


class OneSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


    # def patch(self, request):
    #     one_sensor = Sensor.obgects.get()
    #     data = request.data
    #     one_sensor.name = data.get("name", one_sensor.name)
    #     one_sensor.description = data.get("description", one_sensor.description)
    #     one_sensor.save()
    #     ser = SensorSerializer(one_sensor)
    #     return Response(ser.data)



class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        return Response({'status': 'OK_measurement'})
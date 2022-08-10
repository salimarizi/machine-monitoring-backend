import wave
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from .serializers import AnomalySerializer
from .models import Anomaly
from django.core.files.storage import default_storage
from pylab import *

class AnomalyView(APIView):
    def show_wave_n_spec(self, sound):
        spf = wave.open(sound,'r')
        sound_info = spf.readframes(-1)
        sound_info = fromstring(sound_info, 'int16')

        f = spf.getframerate()
    
        subplot(211)
        plot(sound_info)
        title('Wave from and spectrogram of')

        subplot(212)
        spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')
    
        show()
        spf.close()

    def get(self, request):
        serializer = AnomalySerializer(Anomaly.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        file = request.FILES['file']
        filename = file.name
        filepath = './uploads/' + filename
        default_storage.save(filepath, file)

        # https://web.archive.org/web/20161203074728/http://jaganadhg.freeflux.net:80/blog/archive/2009/09/09/plotting-wave-form-and-spectrogram-the-pure-python-way.html
        # self.show_wave_n_spec(file)

        anomaly_data = Anomaly.objects.create(
            timestamp = datetime.datetime.strptime(request.data['timestamp'], "%Y-%m-%d %H:%M:%S"),
            machine = request.data['machine'],
            anomaly = request.data['anomaly'],
            sensor = request.data['sensor'],
            sound_clip = filename
        )

        serializer = AnomalySerializer(anomaly_data, many=False)

        return Response(serializer.data)

    def patch(self, request):
        anomalies = Anomaly.objects.all()
        for anomaly in anomalies:
            ser_anomaly = AnomalySerializer(anomaly, many=False)
            if ser_anomaly.data['_id'] == request.data['_id']:
                anomaly.reason = request.data['reason']
                anomaly.action = request.data['action']
                anomaly.comments = request.data['comments']
                anomaly.save()

                serializer = AnomalySerializer(anomaly, many=False)
                return Response(serializer.data)

        return Response("Object not found")
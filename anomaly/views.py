import wave
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from random import randint

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from .serializers import AnomalySerializer
from .models import Anomaly
from django.core.files.storage import default_storage
from pylab import *

class AnomalyView(APIView):
    def show_wave_n_spec(self, sound, filename):
        # https://learnpython.com/blog/plot-waveform-in-python/

        wav_obj = wave.open(sound, 'rb')
        sample_freq = wav_obj.getframerate()
        n_samples = wav_obj.getnframes()
        t_audio = n_samples / sample_freq
        
        signal_wave = wav_obj.readframes(n_samples)
        signal_array = np.frombuffer(signal_wave, dtype = np.int16)
        l_channel = signal_array[0::2]
        
        wave_filename = 'wave_' + filename + '.png'
        times = np.linspace(0, t_audio, num=n_samples)
        plt.figure(figsize=(15, 5))
        plt.plot(times, l_channel)
        plt.xlim(0, t_audio)
        plt.savefig('./uploads/' + wave_filename)
        
        specto_filename = 'specto_' + filename + '.png'
        plt.figure(figsize=(15, 5))
        plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
        plt.xlim(0, t_audio)
        plt.colorbar()
        plt.savefig('./uploads/' + specto_filename)

        return [wave_filename, specto_filename]

    def get(self, request):
        serializer = AnomalySerializer(Anomaly.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        file = request.FILES['file']
        filename = str(randint(1000, 9999)) + '.wav'
        filepath = './uploads/' + filename
        default_storage.save(filepath, file)

        # https://web.archive.org/web/20161203074728/http://jaganadhg.freeflux.net:80/blog/archive/2009/09/09/plotting-wave-form-and-spectrogram-the-pure-python-way.html
        [wave, spectogram] = self.show_wave_n_spec(file, filename)

        anomaly_data = Anomaly.objects.create(
            timestamp = datetime.datetime.strptime(request.data['timestamp'], "%Y-%m-%d %H:%M:%S"),
            machine = request.data['machine'],
            anomaly = request.data['anomaly'],
            sensor = request.data['sensor'],
            sound_clip = filename,
            wave = wave,
            spectogram = spectogram
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
import sounddevice as sd
import scipy.io as sio
import scipy.io.wavfile

import sounddevice as sd

samplerate, data = sio.wavfile.read('audio/Faded.wav')

sd.play(data, samplerate)

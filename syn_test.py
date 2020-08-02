from pydub import AudioSegment
from playsound import playsound



t1 = 5536

newAudio1 = AudioSegment.from_wav("audio_change/Faded_95.wav")
newAudio1 = newAudio1[t1:]

t2 = 30576
newAudio2 = AudioSegment.from_wav("audio_change/TheMiddle_95.wav")
newAudio2 = newAudio2[t2:]


newAudio1.export('Mix1.wav', format="wav")
newAudio2.export('Mix2.wav', format="wav")

playsound("Mix1.wav", block=False)
playsound("Mix2.wav", block=False)

import numpy as np
from scipy.io import wavfile
from scipy import interpolate
from scipy.io.wavfile import read as read_wav

NEW_SAMPLERATE = 16000

old_samplerate, old_audio = wavfile.read("out.wav")
print (old_audio)
if old_samplerate != NEW_SAMPLERATE:
    duration = old_audio.shape[0] / old_samplerate

    time_old  = np.linspace(0, duration, old_audio.shape[0])
    time_new  = np.linspace(0, duration, int(old_audio.shape[0] * NEW_SAMPLERATE / old_samplerate))

    interpolator = interpolate.interp1d(time_old, old_audio.T)
    new_audio = interpolator(time_new).T

    wavfile.write("sci.wav", NEW_SAMPLERATE, np.round(new_audio).astype(old_audio.dtype))

sampling_rate, data=read_wav("sci.wav") # enter your filename
print (sampling_rate)
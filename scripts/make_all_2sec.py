import numpy as np
import random
import itertools
import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt
import soundfile as sf
import os
from scipy.io import wavfile

def load_audio_file(file_path):
    output_length = 96000
    data = librosa.core.load(file_path,sr=48000)[0] #, sr=16000
    # samplerate, data = wavfile.read(file_path)
    print (len(data))
    differece = output_length - len(data)
    differece2 = differece
    # wn = np.random.randn(int(len(differece)/2))
    # data_wn = data + 0.01*wn
    if len(data)<output_length:
        
        if differece%2 != 0:
            differece = int(differece/2)
            differece2 = differece+1
        else:
            differece = int(differece/2)
            differece2 = differece
        data = np.pad(data,(differece,differece2), "constant")
        print ("main")
    else:
        print ("in")
    return data

def load(file_path):
    data = librosa.core.load(file_path,sr=48000)[0] #, sr=16000
    return data

def plot_time_series(data):
    # fig = plt.figure(figsize=(14, 8))
    plt.title('Raw wave ')
    plt.ylabel('Amplitude')
    plt.plot(np.linspace(0, 1, len(data)), data)
    plt.show()

# if __name__ == "__main__":
#     name = "test_file/13.wav"
#     data = load_audio_file(name)
#     print (len(data))
#     plot_time_series(data)
#     # sf.write("new"+name, data,48000)
#     f = sf.SoundFile(name)
#     duration = len(f)/f.samplerate
#     print (duration)
#     print (f.samplerate)

if __name__ == "__main__":
    dir = "2_sec_gunshot"
    out_dir = "all_2sec_gunshot"
    for filename in os.listdir(dir):
        full_name = dir+"/"+filename
        data = load_audio_file(full_name)
        print (len(data))
        sf.write(out_dir+"/"+filename, data,48000)

# if __name__ == "__main__":
#     data = load("all_2sec/12092.wav")
#     plot_time_series(data)
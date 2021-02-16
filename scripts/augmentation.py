import numpy as np
import random
import itertools
import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt
import soundfile as sf
import os

def load_audio_file(file_path):
    # input_length = 16000
    data = librosa.core.load(file_path,sr=16000)[0] #, sr=16000
    print (len(data))
    # if len(data)>input_length:
    #     data = data[:input_length]
    # else:
    #     data = np.pad(data, (0, max(0, input_length - len(data))), "constant")
    return data

def plot_time_series(data):
    # fig = plt.figure(figsize=(14, 8))
    plt.title('Raw wave ')
    plt.ylabel('Amplitude')
    plt.plot(np.linspace(0, 1, len(data)), data)
    plt.show()


    

def noise(data):
    wn = np.random.randn(len(data))
    data_wn = data + 0.01*wn
    return data_wn

def roll(data):
    data_roll = np.roll(data, 6000)
    return data_roll

def roll2(data):
    data_roll = np.roll(data, 10000)
    return data_roll

def stretch(data, rate=1):
    # input_length = 16000
    data = librosa.effects.time_stretch(data, rate)
    # if len(data)>input_length:
    #     data = data[:input_length]
    # else:
    #     data = np.pad(data, (0, max(0, input_length - len(data))), "constant")
    return data

def pitch(data):
    data = librosa.effects.pitch_shift(data, len(data), 10)
    return data

def noise_roll(data):
    data = noise(data)
    data = roll(data)
    return data

def noise_stretch(data):
    data = stretch(data, 0.75)
    data = noise(data)
    return data

def noise_pitch(data):
    data = pitch(data)
    data = noise(data)
    return data

def noise_stretch2(data):
    data = noise(data)
    data = stretch(data, 1.2)
    return data

def roll_stretch(data):
    data = roll(data)
    data = stretch(data, 0.75)
    return data

def roll_stretch3(data):
    data = roll2(data)
    data = stretch(data, 0.75)
    return data

def roll_stretch2(data):
    data = roll(data)
    data = stretch(data, 1.2)
    return data

def roll_stretch4(data):
    data = roll2(data)
    data = stretch(data, 1.2)
    return data

def roll_pitch(data):
    data = roll(data)
    data = pitch(data)
    return data

# def stretch_pitch(data):
#     data = stretch(data, 0.75)
#     data = pitch(data)
#     return data

# def stretch_pitch2(data):
#     data = stretch(data, 1.2)
#     data = pitch(data)
#     return data

def noise_roll_stretch(data):
    data = noise_roll(data)
    data = stretch(data, 0.75)
    return data

def noise_roll_stretch2(data):
    data = noise_roll(data)
    data = stretch(data, 1.2)
    return data

def all_function(name,dir):
    
    data = load_audio_file(dir+"/"+name)
    dir = dir+"_new"
    sf.write(dir+"/"+name, data,16000)
    sf.write(dir+"/2"+name, data,16000)
    # data_noise = noise(data)
    # sf.write(dir+"/noise_"+name, data_noise,16000)
    data_roll = roll(data)
    sf.write(dir+"/roll_"+name, data_roll,16000)
    data_roll = roll2(data)
    sf.write(dir+"/2roll_"+name, data_roll,16000)
    
    # data_stretch = stretch(data,0.75)
    # sf.write(dir+"/stretch_"+name, data_stretch,16000)
    # data_stretch2 = stretch(data,1.2)
    # sf.write(dir+"/stretch2_"+name, data_stretch2,16000)
    data_pitch = pitch(data)
    sf.write(dir+"/pitch_"+name, data_pitch,16000)
    sf.write(dir+"/2pitch_"+name, data_pitch,16000)
    # data_noise_roll = noise_roll(data)
    # sf.write(dir+"/noise_roll_"+name, data_noise_roll,16000)
    # data_noise_stretch = noise_stretch(data)
    # sf.write(dir+"/noise_stretch_"+name, data_noise_stretch,16000)
    # data_noise_stretch2 = noise_stretch2(data)
    # sf.write(dir+"/noise_stretch2_"+name, data_noise_stretch2,16000)
    # data_noise_pitch = noise_pitch(data)
    # sf.write(dir+"/noise_pitch_"+name, data_noise_pitch,16000)
    # data_roll_stretch = roll_stretch(data)
    # sf.write(dir+"/roll_stretch_"+name, data_roll_stretch,16000)
    # data_roll_stretch2 = roll_stretch(data)
    # sf.write(dir+"/roll_stretch2_"+name, data_roll_stretch2,16000)
    # data_roll_pitch = roll_pitch(data)
    # sf.write(dir+"/roll_pitch_"+name, data_roll_pitch,16000)
    # data_noise_roll_stretch = noise_roll_stretch(data)
    # sf.write(dir+"/noise_roll_stretch_"+name, data_noise_roll_stretch,16000)
    # data_noise_roll_stretch2 = noise_roll_stretch2(data)
    # sf.write(dir+"/noise_roll_stretch2_"+name, data_noise_roll_stretch2,16000)
    # data_roll2 = roll2(data)
    # sf.write(dir+"/roll2_"+name, data_roll2,16000)
    # data_roll_stretch3 = roll_stretch3(data)
    # sf.write(dir+"/roll_stretch3_"+name, data_roll_stretch3,16000)
    # data_roll_stretch4 = roll_stretch4(data)
    # sf.write(dir+"/roll_stretch4_"+name, data_roll_stretch4,16000)






# if __name__ == "__main__":
#     data = load_audio_file("glass/1-85184-A-39.wav")
#     plot_time_series(data)
#     sf.write('original.wav', data,len(data))
#     # ipd.Audio(data, rate=16000)
#     wn = np.random.randn(len(data))
#     data_wn = data + 0.01*wn
#     sf.write('noise.wav', data_wn,16000)
#     plot_time_series(data_wn)
#     # We limited the amplitude of the noise so we can still hear the word even with the noise, 
#     #which is the objective
#     # ipd.Audio(data_wn, rate=16000)
#     # print ("test")
#     data_roll = np.roll(data, 1600)
#     sf.write('roll.wav', data_roll,16000)
#     plot_time_series(data_roll)
#     # ipd.Audio(data_roll, rate=16000)
#     data_stretch =stretch(data, 0.7)
#     print (len(data_stretch))
#     sf.write('stretch.wav', data_stretch, 16000)
#     print("This makes the sound deeper but we can still hear 'off' ")
#     plot_time_series(data_stretch)
#     # ipd.Audio(data_stretch, rate=16000)

#     data_stretch =stretch(data, 1.3)
#     print("Higher frequencies  ")
#     plot_time_series(data_stretch)
#     sf.write('stretch2.wav', data_stretch, 16000)
#     ipd.Audio(data_stretch, rate=16000,autoplay=True)
#     data = librosa.effects.pitch_shift(data, len(data), 10)
#     plot_time_series(data)
#     print (len(data))

if __name__ == "__main__":
    # for filename in os.listdir("glass"):
    #     all_function(filename,"glass")
    for filename in os.listdir("transfer_learning_data/sneeze"):
        all_function(filename,"transfer_learning_data/sneeze")
    # for filename in os.listdir("gun_shot"):
    #     all_function(filename,"gun_shot")
import soundfile as sf
import os
from shutil import copyfile

dir = "train_dataset_cough_gunshot/sneeze"
duration_2 = 0
count = 0
for filename in os.listdir(dir):
    print (filename)
    name = dir+"/"+filename
    f = sf.SoundFile(name)
    # print(float(len(f))/float(f.samplerate))
    # print (len(f))
    # print (f)
    print (f.samplerate)
    duration = float(len(f))/float(f.samplerate)
    # if duration<=2:
    #     duration_2=duration_2+1
    #     dst = "2_sec_gunshot"+"/"+filename
    #     copyfile(name, dst)
    #     print (filename)
    if duration<=2:
        count = count+1

print (count)
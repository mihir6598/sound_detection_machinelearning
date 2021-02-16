import os 
from pydub import AudioSegment

dir = "neg"
out_dir = "neg_new"
count = 1
for filename in os.listdir(dir):
    print (filename)
    src = dir+"/"+filename
    dst = str(count)+".wav"
    count = count + 1
    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    print (count)
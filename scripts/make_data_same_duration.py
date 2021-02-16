import numpy as np

def make_16000(data):
    output_length = 16000
    if len(data)<output_length:
        differece = output_length - len(data)
        differece2 = differece
        if differece%2 != 0:
            differece = int(differece/2)
            differece2 = differece+1
        else:
            differece = int(differece/2)
            differece2 = differece
        data = np.pad(data,(differece,differece2), "constant")
        print ("less")
    else:
        data = data[0:16000]
        print ("more")
    return data
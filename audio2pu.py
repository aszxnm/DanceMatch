import os
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('Agg') # No pictures displayed 
import pylab
import librosa
import librosa.display
import numpy as np

sig, fs = librosa.load('./audio1.wav')   
# make pictures name 
save_path = 'test.jpg'

#pylab.axis('off') # no axis
pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
S = librosa.feature.melspectrogram(y=sig[:16000], sr=16000, n_fft=1024, hop_length=512, n_mels=128)
S = librosa.power_to_db(S, ref=np.max)
print(S.shape)
librosa.display.specshow(S, x_axis='time', y_axis='mel')
pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
pylab.close()
import h5py
import numpy as np

f = h5py.File("vgg_c10_weights.h5", 'r')
#f = h5py.File("compressed_vgg_weights.h5", 'r')
#weight=f['conv2d_4']['conv2d_4']['kernel:0'][:]
weight=f['dense_2']['dense_2']['kernel:0'][:]
#Transform the four-dimensional array of weights into one-dimensional array
arr=[*weight.flat]
print(arr)
#View key
for key in f:
    print("key : " + key)

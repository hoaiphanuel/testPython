import epochs as epochs
import tensorflow as tf
import numpy as np
from tensorflow import keras
import time
import matplotlib.pyplot as plt
import imageio
import random
#du lieu ham y=x*2
x = np.arange(-1, 1, 0.01)
y = x*2
print(x)
print(y)
#gay nhiểu y
y = y+ np.random.uniform(-0.03,0.03,x.shape)
print(y)


xs = np.array(x,dtype=float)
ys = np.array(y,dtype=float)


model = keras.Sequential([keras.layers.Dense(units=1,input_shape=[1])])
model.compile(optimizer="sgd",loss="mean_squared_error")

model.fit(xs,ys,epochs=500)


print(model.predict([10]))

#Import required Libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras

x = np.arange(0, 1, 0.001)
y = x*2
y = np.add(y,np.random.uniform(-0.03,0.03))
print(y)
# tao dự liệu cho training
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest= train_test_split(x,y,test_size=0.2)
#tfe = tf.config.experimental_functions_run_eagerly()
W = tf.Variable([1])
b = tf.Variable(np.random.uniform(-2,2))
def LinearRegression(inputs):
    return (tf.matmul(inputs, W, transpose_b = True))

def LossFunction(model_fn,inputs,labels):
    return tf.reduce_mean(tf.square(model_fn(inputs)-labels))

learning_rate=0.01
number_step = 1000
optimizer = keras.optimizers.SGD(learning_rate=learning_rate)
#caculate gradient
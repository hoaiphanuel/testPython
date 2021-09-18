import tensorflow as tf
import numpy as np
import pandas as pd
from pylab import rcParams
import matplotlib.pyplot as plt
import warnings
#matplotlib inline
warnings.filterwarnings("ignore")
pd.set_option('display.expand_frame_repr', False)
# frame window
rcParams['figure.figsize'] = 10, 5
df = pd.read_csv("data/data.csv")
print (df.head)
X=df["X"]
Y=df["y"]
plt.scatter(df["X"], df["y"])
plt.show()
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_shape=[1]))
#model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.01))
# không hiệu quả
model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.SGD(learning_rate=0.1))
#model.compile(optimizer='sgd',loss='mean_squared_error' )

print(model.summary())

history = model.fit(X, Y, epochs=300)
plt.plot(history.history['loss'])
plt.show()
#X=[1]
df["prediction"] = model.predict(X)
print(df["prediction"])
#plt.scatter(df["X"], df["y"])
#plt.plot(X, df["prediction"], color='r')
#plt.show()
print(model.predict([10.1]))
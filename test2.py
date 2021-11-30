import tensorflow as tf


layer = tf.keras.layers.Dense(32, activation='relu')
inputs = tf.random.uniform(shape=(10, 20))
outputs = layer(inputs)
print(outputs)

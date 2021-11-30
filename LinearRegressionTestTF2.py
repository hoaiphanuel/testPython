import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

"""Now we will define model and loss function"""

# Define a Linear model
class LinearModel(object):
    def __init__(self):
        self.W = tf.Variable(0.0)
        self.b = tf.Variable(0.0)

    def __call__(self, inputs):
        return self.W * inputs + self.b

#Define Loss Function
def compute_loss(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true-y_pred))

"""Initialize our linear regression model.

"""

#Instantiate Linear Regression Model
model = LinearModel()

"""Define weight and bias for the model"""

# Define the weight and bias
weight = 2
bias = 1.0

"""Prepare Training Data"""
"""
# Generate Data
data = 100
inputs  = tf.random.normal(shape=[data])
noise   = tf.random.normal(shape=[data])
outputs = inputs * weight + bias + noise
"""
inputs =np.arange(-3,3,0.01)
data = inputs.shape
outputs=inputs*weight+bias
outputs=outputs+np.random.uniform(-0.3,0.3,inputs.shape)
#y=20x+1

"""Check Generated data:

"""

print(inputs)

"""Print noise data:

"""

#print(noise)

"""Print outputs:"""

print(outputs)

"""Define the data visualizatin function to be used to display graph during training."""

# Model visualization function to generate graph during training
def plot(epoch):
    plt.scatter(inputs, outputs, c='b')
    #plt.scatter(inputs, model(inputs), c='m')
    plt.plot(inputs, model(inputs),  c='r', label ='Fitted line')
    plt.title("epoch %2d, loss = %s" %(epoch, str(compute_loss(outputs, model(inputs)).numpy())))
    plt.legend()
    plt.draw()
    plt.ion()
    plt.pause(1)
    plt.close()

"""Training Loop"""

Ws, bs = [], []

epochs = range(50)

# Define a training loop
learning_rate = 0.1

for epoch in epochs:
    with tf.GradientTape() as tape:
        loss = compute_loss(outputs, model(inputs))

    dW, db = tape.gradient(loss, [model.W, model.b])

    Ws.append(model.W.numpy())
    bs.append(model.b.numpy())

    model.W.assign_sub(learning_rate * dW)
    model.b.assign_sub(learning_rate * db)

    print("=> epoch %2d: w_true= %.2f, w_pred= %.2f; b_true= %.2f, b_pred= %.2f, loss= %.2f" %(
          epoch+1, weight, model.W.numpy(), bias, model.b.numpy(), loss.numpy()))
    if (epoch) % 2 == 0: plot(epoch + 1)

"""Plot"""

# Show all
plt.plot(epochs, Ws, 'r',
         epochs, bs, 'b')
plt.plot([weight] * len(epochs), 'r--',
         [bias] * len(epochs), 'b--')
plt.legend(['W', 'b', 'true W', 'true_b'])
plt.show()
x = 4
print (Ws[48]*x+bs[48])
# Data
In this project I am trying to predict whether or not a single number
is either a 1 or a 0. Our input vector is a single dimension of size 1
which contains a float. Our output vector is a single dimensional vector which contains a number closer to 1 or closer to 0.

# Model
For this I will be using a Sequential model from the Keras library set of models. This model is composed of three dense layers. The first and second contain 32 neurons. The last contains 1 neuron for the prediction.

# Activations
The layers in our network are activated using tanh. Tanh will squash the value between 0 and 1.

# Error
The error is calculated by using Mean Absolute Error.

# Optimizer
The optimizer we use is RMSprop.

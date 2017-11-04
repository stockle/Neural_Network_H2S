# Neural Network H2S

SO YOU WANT TO MAKE A NEURAL Network

You've come to the right place. For these exercises we will be using the [Keras machine learning library](https://keras.io/).

# Formatting

It is very important to format your code in an accessible and organized way. This is very important when explaining your code, even more important when you are not there to explain it.

## Network Formatting

For every exercise you will return a classes.py file which will contain relevant classes. The formatting of any extra class is left to you. Try to keep it aligned in a similar format to the one mandatory class defined below:

```python
# Define your network below
# This is a comment. Replace comments with YOUR code
'''This is also a comment'''
'''Sometimes you may want to pass variables to an object's
    method. Sometimes you may just want to do everything
    inside that method. The choice is up to you...'''

class Network():
	def __init__(self,
              # useful_variable_1,
              # useful_variable_2
              ):
    # initialize variables you find important
	def _build_model(self,
                  # useful_variable_1,
                  # useful_variable_2
                  ):
    # assemble your model here.
    # return the model after assembly
    # be careful with your dimension sizes and pay attention
    #   to your activation functions
	def fit(self,
          # useful_variable_1,
          # useful_variable_2
          ):
		# this is your training method
    # it will train the model on some data.
	def predict(self, X):
		# return the prediction of some data
	def load(self, name):
		# load the weights from a trained.h5 file
	def save(self, name):
		# save the weights to a trained.h5 file
```

## Data Formatting

Data should be in csv(comma-separated value). Example below:

```
X0,X1,X2,Y0
0,0,1,1
1,1,0,0
0,0,1,1
0,0,1,1
1,1,0,0
```

Rows indicate a set of valid data. Columns indicate what that data is. Label your data with succinct names that allow users to identify what that data is.

# ex00 - 101010

In this exercise you will be predicting whether or not a number is a 0 or a 1. Sounds easy, right? There's a lot of work behind the libraries that make these predictions possible. For now you will be learning basic data manipulation, formatting, and how to use the Keras library.

## directories to turn in
 - data
## files to turn in
 - run.py
 - classes.py
 - trained.h5
 - data/numbers.csv

# ex01 - Thinking Bigger

# ex02 - Arrays

# ex03 - Images

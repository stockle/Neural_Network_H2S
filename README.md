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
0,0,1,1
1,1,0,0
0,0,1,1
0,0,1,1
1,1,0,0
...
```

Rows indicate a set of valid data. Columns indicate what that data is. For all of your datasets there should be at least 300 training examples.

# ex00 - 101010

In this exercise you will be classifying whether or not a number is a 0 or a 1. Sounds easy, right? There's a lot of work behind the libraries that make these classifications possible. For now you will be learning basic data manipulation, formatting, and how to use the Keras library.

```
$> python run.py --predict 1
$> 1.0
$> python run.py --predict 0
$> 4.51851e-13
$> python run.py --predict 5
$> Error
```

## directories to turn in
 - ex00
## subdirectories to turn in
 - data
## files to turn in
 - run.py
 - classes.py
 - trained.h5
 - data/numbers.csv

# ex01 - Thinking Bigger

This exercise will be the same as the previous one. You are predicting what a number is, WITH A TWIST. Turns out there are more numbers than 0 and 1(big shocker). You will be classifying a number between 0 and 9. There are many ways to do this. I recommend experimenting.

```
$> python run.py --predict 5
$> 4.9957
$> python run.py --predict 9
$> 8.99301
$> python run.py --predict 42
$> Error
$> python run.py --predict
$>
```

## directories to turn in
 - ex01
## subdirectories to turn in
 - data
## files to turn in
 - run.py
 - classes.py
 - trained.h5
 - data/numbers.csv

# ex02 - Arrays

For this exercise your network will learn to recognize the largest number in an array. This time you will be processing an entire array at once instead of a single digit. Pay attention to data formatting, access, and manipulation; they may give you headaches at first, but it's very good knowledge to have!

```
$> python run.py --predict 1234567890
$> 8.42899
$> python run.py --predict 4862135878
$> 9.03341
$> python run.py --predict 0005000000
$> 4.93534
$> python run.py --predict 12345678901234
$> Error
$> python run.py --predict
$>
```

As you can see, the algorithm will not always be entirely accurate. This could be due to a number of factors. The algorithm generalizing towards an accurate guess rather than a one-to-one decision is what makes neural networks both relatable and mysterious. How can you improve your accuracy? Why do you think the algorithm chose the way it did? Why do you think the algorithm loses accuracy on data of this structure?

## directories to turn in
 - ex02
## subdirectories to turn in
 - data
## files to turn in
 - run.py
 - classes.py
 - trained.h5
 - data/numbers.csv

# ex03 - Images

For this exercise we will be classifying from the [MNIST handwritten digit dataset](http://yann.lecun.com/exdb/mnist/). You will need to design a Convolutional Neural Network to scan a two-dimensional image and classify which digit it represents. Your program will take similar arguments, just like before, but this time you will need to load the appropriate image from the appropriate folder and then classifiy that image, returning the result on the command line.

```
$> python run.py --predict 1
$> 1
$> python run.py --predict 5
$> 5
$> python run.py --predict 8
$> 8
$> python run.py --predict 42
$> Error
```

## directories to turn in
 - ex03
## subdirectories to turn in
 - data
 - data/images
 - data/images/0
 - data/images/1
 - data/images/...
 - data/images/9
## files to turn in
 - run.py
 - classes.py
 - trained.h5

# ex04 - YOU

What kind of data interests you? How can machines learning help you analyze data more efficiently? You have a lot of freedom with this exercise but we suggest you maintain the structure you've been working with. If you find yourself with cluttered files, break them up into smaller, functional files, named appropriately of course.

## directories to turn in
 - ex04
## subdirectories to turn in
 - data
 - data/ ~useful subdirectories
## files to turn in
 - run.py
 - classes.py
 - trained.h5
 - ~ other_files.py

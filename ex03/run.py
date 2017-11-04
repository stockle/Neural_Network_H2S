from sklearn.model_selection import train_test_split
from keras.datasets import mnist
from keras.utils import np_utils
from keras import backend as K
import numpy as np
import classes
import cv2
import sys
import os

EPOCHS = 1

K.set_image_dim_ordering('th')

def average(pixel):
    return np.average(pixel)

def run(args, network):
	if args[1] == '--train' and len(args) == 2:
		print "Training ..."
		for i in range(EPOCHS):
			(X, Y), (x, y) = mnist.load_data()
			X_ = X.reshape(X.shape[0], 1, 28, 28).astype('float32')
			x_ = x.reshape(x.shape[0], 1, 28, 28).astype('float32')
			X_ = X_ / 255
			x_ = x_ / 255
			Y_ = np_utils.to_categorical(Y)
			y_ = np_utils.to_categorical(y)
			network.fit(X_, Y_, x_, y_)
		network.save('trained.h5')
	elif args[1] == '--predict' and len(args) == 3:
		P = np.empty((28, 28))
		result = []
		if args[2] == '0':
			im = cv2.imread('data/images/0/10.png')
		elif args[2] == '1':
			im = cv2.imread('data/images/1/14.png')
		elif args[2] == '2':
			im = cv2.imread('data/images/2/1.png')
		elif args[2] == '3':
			im = cv2.imread('data/images/3/18.png')
		elif args[2] == '4':
			im = cv2.imread('data/images/4/4.png')
		elif args[2] == '5':
			im = cv2.cv2.imread('data/images/5/8.png')
		elif args[2] == '6':
			im = cv2.imread('data/images/6/11.png')
		elif args[2] == '7':
			im = cv2.imread('data/images/7/0.png')
		elif args[2] == '8':
			im = cv2.imread('data/images/8/61.png')
		elif args[2] == '9':
			im = cv2.imread('data/images/9/9.png')
		else:
			print "Error"
			return
		grey = np.zeros((im.shape[0], im.shape[1]))
		for rownum in range(len(im)):
			for colnum in range(len(im[rownum])):
				grey[rownum][colnum] = average(im[rownum][colnum])
		P[0:28, 0:28] = grey
		P_ = np.reshape(P, (1, 1, 28, 28))
		result = network.predict(P_)[0]
		for i in range(len(result)):
			if result[i] == 1:
				print i

	else:
		print 'Unknown command'
		return
	print "Arguments Processed!"

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        network = classes.Network(10)
        if os.path.exists('trained.h5'):
            network.load('trained.h5')
        run(sys.argv, network)
    else:
        print "Options: python run.py --train\n\
         python run.py --predict <number>"

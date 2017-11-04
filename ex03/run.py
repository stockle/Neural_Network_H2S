from sklearn.model_selection import train_test_split
from keras.datasets import mnist
from keras.utils import np_utils
from keras import backend as K
import numpy as np
import classes
import sys
import os

EPOCHS = 1

K.set_image_dim_ordering('th')

def run(args, network):
	if args[1] == '--train':
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
	elif args[1] == '--predict':
		if args[2] == '0':
			im = imread('data/images/0/10.png')
			im = im / 255
			print network.predict(im)
		elif args[2] == '1':
			im = imread('data/images/1/14.png')
        	        im = im / 255
        	        print network.predict(im)
		elif args[2] == '2':
			im = imread('data/images/2/1.png')
        	        im = im / 255
        	        print network.predict(im)
		elif args[2] == '3':
			im = imread('data/images/3/18.png')
			im = im / 255
			print network.predict(im)
		elif args[2] == '4':
			im = imread('data/images/4/4.png')
	                im = im / 255
        	        print network.predict(im)
		elif args[2] == '5':
			im = imread('data/images/5/8.png')
	                im = im / 255
	                print network.predict(im)
		elif args[2] == '6':
			im = imread('data/images/6/11.png')
        	        im = im / 255
        	        print network.predict(im)
		elif args[2] == '7':
			im = imread('data/images/7/0.png')
        	        im = im / 255
			print network.predict(im)
		elif args[2] == '8':
			im = imread('data/images/8/61.png')
	                im = im / 255
	                print network.predict(im)
		elif args[2] == '9':
			im = imread('data/images/9/9.png')
        	        im = im / 255
        	        print network.predict(im)

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

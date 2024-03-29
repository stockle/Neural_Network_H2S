#from sklearn.model_selection import train_test_split
from keras.datasets import mnist
import numpy as np
import classes
import sys
import os

EPOCHS = 42

def get_inputs(path):
	seed = 42
	ran = np.random.seed(seed)
	dataset = np.loadtxt(path, delimiter=',')
	X = dataset[:,0:10].astype(np.float)
	Y = dataset[:,10:].astype(np.float)
	(X_, x, Y_, y) = train_test_split(X, Y, test_size=0.33, random_state=seed)
	return (X_, x, Y_, y)

def run(args, network):
	if args[1] == '--train' and len(args) == 2:
		print "Training ..."
		for i in range(EPOCHS):
			(X, x, Y, y) = get_inputs('data/numbers.csv')
			network.fit(X, Y, x, y)
		network.save('trained.h5')
	elif args[1] == '--predict' and len(args) == 3:
		if len(args[2]) == 10:
			M = []
			for i in args[2]:
				M.append(float(i))
			T = np.array([M])
			P = list(network.predict(T)[0])[0]
			print P
		else:
			print "Error"
			return
	else:
		print "Error"
		return
	print "Arguments Processed!"

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        network = classes.Network(10, 1)
        if os.path.exists('trained.h5'):
            network.load('trained.h5')
        run(sys.argv, network)
    else:
        print "Options: python run.py --train\n\
         python run.py --predict <value>"

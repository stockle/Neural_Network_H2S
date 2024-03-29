from sklearn.model_selection import train_test_split
import numpy as np
import classes
import sys
import os

EPOCHS = 42

def get_inputs(path):
	seed = 42
	ran = np.random.seed(seed)
	dataset = np.loadtxt(path, delimiter=',')
	X = dataset[1:,0:1].astype(np.float)
	Y = dataset[1:,1:].astype(np.float)
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
		if args[2] == '1' or args[2] == '0':
			M = [float(args[2])]
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
        network = classes.Network(1, 1)
        if os.path.exists('trained.h5'):
            network.load('trained.h5')
        run(sys.argv, network)
    else:
        print "Options: python run.py --train\n\
         python run.py --predict <value>"

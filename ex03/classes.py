from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Activation,\
			Dense,\
			Conv2D,\
			MaxPooling2D,\
			Flatten,\
			Dropout
import keras
import numpy as np

class Network():
	def __init__(self, output):
		self.output_size = output
		self.model = self._build_model()
	def _build_model(self):
		model = Sequential()
		model.add(Conv2D(32, (3, 3), input_shape=(1, 28, 28), data_format='channels_first'))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))

		model.add(Conv2D(32, (3, 3), data_format='channels_first'))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))

		model.add(Conv2D(64, (3, 3), data_format='channels_first'))
		model.add(Activation('relu'))
		model.add(MaxPooling2D(pool_size=(2, 2)))

		model.add(Flatten())
		model.add(Dense(64))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))
		model.add(Dense(self.output_size))
		model.add(Activation('relu'))

		model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
		return model
	def fit(self, inputs, target, valid_inputs, valid_target):
		self.model.fit(
			inputs,
			target,
			validation_data=(valid_inputs, valid_target),
			epochs=10,
			batch_size=64,
			verbose=0)
	def predict(self, X):
		return self.model.predict(X)
	def load(self, name):
		self.model.load_weights(name)
	def save(self, name):
		self.model.save_weights(name)

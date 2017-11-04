from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers import Activation, Dense
import keras
import numpy as np

class Network():
	def __init__(self, inputs, outputs):
		self.input_size = inputs
		self.output_size = outputs
		self.model = self._build_model()
	def _build_model(self):
		keras.initializers.Constant(value=0)
		model = Sequential()
		model.add(Dense(32, input_dim=self.input_size, activation='linear'))
		model.add(Dense(32, activation='linear'))
		model.add(Dense(self.output_size, activation='linear'))
		model.compile(loss='mean_absolute_error', optimizer='Adam', metrics=['accuracy'])
		return model
	def fit(self, inputs, target, valid_inputs, valid_target):
		self.model.fit(
			inputs,
			target,
			validation_data=(valid_inputs, valid_target),
			epochs=100,
			batch_size=64,
			verbose=0)
	def predict(self, X):
		return self.model.predict(X)
	def load(self, name):
		self.model.load_weights(name)
	def save(self, name):
		self.model.save_weights(name)

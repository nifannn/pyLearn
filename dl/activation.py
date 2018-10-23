import numpy as np


def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def sigmoid_grad(y):
	return y * (1 + y)

def relu(x):
	return np.max(0, x)

def relu_grad(y):
	pass


FORWARD_FUN = {
	'sigmoid': sigmoid,
	'relu': relu
}

BACKPROP_FUN = {
	'sigmoid': sigmoid_grad,
	'relu': relu_grad
}


class Activation(object):
	"""docstring for Sigmoid"""
	
	def __init__(self, name):
		self.name = name

	def _forward(self, x):
		return FORWARD_FUN[self.name](x)

	def _backward(self, y):
		return BACKPROP_FUN[self.name](y)
		


class Dense(object):
	"""docstring for Dense"""
	def __init__(self, units, activation='relu', input_dim=None, name=None):
		self._units = units
		self._activation = activation
		self._input_dim = input_dim

	def _init_weights(self):
		pass

	def _forward(self, x):
		pass

	def _compute_grad(self):
		pass

	def _update_weights(self):
		pass
		
	@property
	def activation(self):
		return self._activation

	@property
	def units(self):
		return self._units

	@property
	def input_dim(self):
		return self._input_dim

	@property
	def value(self):
		return self._value

	@property
	def grad(self):
		return self._grad
	
	
	
	
	
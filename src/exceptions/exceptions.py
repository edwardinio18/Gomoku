"""
	Exceptions
"""


class CustomException(Exception):
	"""
		Custom exception class
	"""

	def __init__(self, msg):
		"""
			Initializing the custom exception class

			:param msg: The error message
		"""

		super().__init__(msg)
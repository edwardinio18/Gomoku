"""
	Board
"""

from src.constants.constants import *


class Board:
	"""
		Board class
	"""

	def __init__(self, typ):
		"""
			Initializes the game board class
		"""

		self.__board = [[typ for j in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]

	def __getitem__(self, tup):
		"""
			Returns the value at a given position on the game board

			:param tup: Tuple of x and y values
			:return: Value at a given position
		"""

		x, y = tup
		return self.__board[x][y]

	def __setitem__(self, tup, value):
		"""
			Sets a new value at a given position on the game board

			:param tup: Tuple of x and y values
			:param value: New value to be sets
		"""

		x, y = tup
		self.__board[x][y] = value

	def __str__(self):
		"""
			Allows for the string interpretation of the board class

			:return: String representation of the board class
		"""

		return str(self.__board)

	def print_board(self):
		"""
			Prints the game board
		"""

		return "\n".join([chr(65 + row) + "".join(["\t" + str(item) for item in self.__board[row]]) for row in
						 range(len(self.__board))]) + "\n\t" + "\t".join([str(i + 1) for i in range(BOARD_SIZE)])

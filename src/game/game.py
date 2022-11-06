"""
	Game
"""

from random import randint

from src.board.board import Board
from src.constants.constants import *


class Game:
	"""
		Game class
	"""

	def __init__(self, typ=None):
		"""
			Initializes the game class for the game
		"""

		self._winner = 0
		self._curr_player = randint(1, 2)
		self._board = Board(typ)
		self._player_1_name = self._player_2_name = ""

	def val_pos(self, pos, typ):
		"""
			Validates the selected position on the board

			:param pos: Position
			:param typ: UI type
			:return: True/False
		"""

		row = pos[0]
		col = pos[1]
		if typ == 0:
			return (not (row < 0 or row > BOARD_SIZE - 1)) and (not (col < 0 or col > BOARD_SIZE - 1)) and (
				not self._board[row, col])
		else:
			return (not (row < 0 or row > BOARD_SIZE - 1)) and (not (col < 0 or col > BOARD_SIZE - 1)) and (
				not (self._board[row, col] != typ))

	def check_winner(self, player, typ, color=None):
		"""
			Checks if a player has won the game

			:param player: Current player
			:param typ: UI type
			:param color: UI user color
			:return: Winning player or 0 (no one has won yet)
		"""

		dirs = ((1, 0), (0, 1), (1, 1), (1, -1))
		for i in range(19):
			for j in range(19):
				if typ == 0:
					if self._board[i, j] != player:
						continue
				else:
					if self._board[i, j] != color:
						continue
				for direc in dirs:
					row, col = i, j
					count = 0
					for k in range(5):
						if typ == 0:
							if col > 18 or col < 0 or row > 18 or row < 0 or self._board[row, col] != player:
								break
						else:
							if col > 18 or col < 0 or row > 18 or row < 0 or self._board[row, col] != color:
								break
						row += direc[0]
						col += direc[1]
						count += 1
					if count == 5:
						return player
		return 0

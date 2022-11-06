"""
	UI
"""

import sys
from random import randint

from termcolor import colored

from src.ai.ai import AI
from src.exceptions.exceptions import CustomException
from src.game.game import Game


class UI:
	"""
		UI class
	"""

	def __init__(self, ai=False):
		"""
			Initializes the UI class
		"""

		self.__game = Game("-")
		self.__ai_choice = ai

		if self.__ai_choice:
			self.__ai = AI()

		self.__player_1_name = self.__game._player_1_name
		if self.__ai_choice:
			self.__ai.rand_name()
			self.__player_2_name = self.__ai._name
		else:
			self.__player_2_name = self.__game._player_2_name
		self.__winner = self.__game._winner
		self.__board_game = self.__game._board
		self.__curr_player = self.__game._curr_player

	def set_player_names(self):
		"""
			Sets both players' names
		"""

		self.__player_1_name = input("Player 1: ")
		self.__player_1_name = self.__player_1_name.capitalize()
		if not self.__ai_choice:
			self.__player_2_name = input("Player 2: ")
			self.__player_2_name = self.__player_2_name.capitalize()
		else:
			print("\nPlayer 2: " + self.__player_2_name)

	def game(self):
		"""
			Handles the game
		"""

		print("\nWelcome to your favorite board game, Gomoku!\n")

		self.set_player_names()

		print("\n" + self.__player_1_name + ", " + self.__player_2_name + ", may the best player win!")

		curr_color = 0
		while True:
			if self.__curr_player == 1:
				self.__curr_player_name = self.__player_1_name
			else:
				self.__curr_player_name = self.__player_2_name

			print("\n" + self.__curr_player_name + "'s turn\n")
			board_print = self.__board_game.print_board()
			print(board_print)
			print("\nWhere would you like to place your piece?")

			if not self.__ai_choice:
				while True:
					pos = input("Position (format = A9): ")
					try:
						if len(pos) < 2 or len(pos) > 3 or not pos[0].isalpha():
							raise CustomException("Invalid input, please try again!")
						if ord(pos[0]) < 65 or ord(pos[0]) > 83:
							raise CustomException("Invalid input, please try again!")
						y = ord(pos[0]) - 65
						pos = pos.split(pos[0], 1)[1]
						if not pos.isdigit():
							raise CustomException("Invalid input, please try again!")
						pos = int(pos)
						if pos not in range(1, 20):
							raise CustomException("Invalid input, please try again!")
						x = pos - 1
						if not self.__game.val_pos((y, x), "-"):
							raise CustomException("Position already occupied, please try again!")
						break
					except CustomException as e:
						print("\n" + str(e))
			else:
				if self.__curr_player == 2:
					y = randint(65, 83) - 65
					x = randint(1, 19)
					while not self.__game.val_pos((y, x - 1), "-"):
						y = randint(65, 83) - 65
						x = randint(1, 19)
					print("Position (format = A9): " + chr(y + 65) + str(x))
				else:
					while True:
						pos = input("Position (format = A9): ")
						try:
							if len(pos) < 2 or len(pos) > 3 or not pos[0].isalpha():
								raise CustomException("Invalid input, please try again!")
							if ord(pos[0]) < 65 or ord(pos[0]) > 83:
								raise CustomException("Invalid input, please try again!")
							y = ord(pos[0]) - 65
							pos = pos.split(pos[0], 1)[1]
							if not pos.isdigit():
								raise CustomException("Invalid input, please try again!")
							pos = int(pos)
							if pos not in range(1, 20):
								raise CustomException("Invalid input, please try again!")
							x = pos - 1
							if not self.__game.val_pos((y, x), "-"):
								raise CustomException("Position already occupied, please try again!")
							break
						except CustomException as e:
							print("\n" + str(e))

			color = [colored(u"\u25CF", "grey"), colored(u"\u25CF", "white")]

			if self.__curr_player == 2 and self.__ai_choice:
				x -= 1
			self.__board_game[y, x] = color[curr_color]

			self.__winner = self.__game.check_winner(self.__curr_player, "-", color[curr_color])

			if self.__winner != 0:
				if self.__winner == 1:
					winner_name = self.__player_1_name
				else:
					winner_name = self.__player_2_name
				board_print = self.__board_game.print_board()
				print("\n" + board_print)
				print("\nCongratulations, " + winner_name + ", you have won the game!")
				while True:
					try:
						print("\nWould you like to play again?")
						cmd = input("Y/N: ")
						if cmd != "Y" and cmd != "N":
							raise CustomException("Invalid input, please try again!")
						if cmd == "Y":
							print("\n" * 100)
							ui = UI(self.__ai_choice)
							ui.start()
						else:
							print("\nHope you enjoyed Gomoku, see you again soon!")
							sys.exit()
						break
					except CustomException as e:
						print("\n" + str(e))
			else:
				if curr_color == 0:
					curr_color = 1
				else:
					curr_color = 0

				if self.__curr_player == 1:
					self.__curr_player = 2
				else:
					self.__curr_player = 1

	def start(self):
		"""
			Starts the game
		"""

		self.game()

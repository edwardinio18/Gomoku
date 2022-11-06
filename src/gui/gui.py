"""
    GUI
"""

import sys
from random import randint

import pygame
from pygame.locals import *

from src.ai.ai import AI
from src.constants.constants import *
from src.game.game import Game


class GUI:
	"""
		GUI class
	"""

	def __init__(self, ai=False):
		"""
			Initializes the GUI class for the game
		"""

		pygame.init()

		pygame.display.set_caption("Gomoku")

		self.__board = pygame.image.load(BOARD_IMG)
		self.__black = pygame.image.load(BLACK_PIECE_IMG)
		self.__white = pygame.image.load(WHITE_PIECE_IMG)

		self.__rate = pygame.time.Clock()
		self.__display = pygame.display.set_mode((GUI_WIDTH, GUI_HEIGHT))

		self.__game = Game(0)
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

	def display_names(self, player):
		"""
			Displays information for the players
		"""

		pygame.draw.rect(self.__display, (195, 195, 195), (0, 0, 200, GUI_HEIGHT))

		if player == PLAYER_1:
			pygame.draw.rect(self.__display, (0, 175, 0),
			                 (PLAYER_INFO_X + 17, PLAYER_1_INFO_Y - 15, INFO_WIDTH - 33, INFO_HEIGHT + 35),
			                 2, 8)
			pygame.draw.rect(self.__display, (0, 0, 0),
			                 (PLAYER_INFO_X + 17, PLAYER_2_INFO_Y - 15, INFO_WIDTH - 33, INFO_HEIGHT + 35),
			                 2, 8)
		else:
			pygame.draw.rect(self.__display, (0, 175, 0),
			                 (PLAYER_INFO_X + 17, PLAYER_2_INFO_Y - 15, INFO_WIDTH - 33, INFO_HEIGHT + 35),
			                 2, 8)
			pygame.draw.rect(self.__display, (0, 0, 0),
			                 (PLAYER_INFO_X + 17, PLAYER_1_INFO_Y - 15, INFO_WIDTH - 33, INFO_HEIGHT + 35),
			                 2, 8)

		font = pygame.font.SysFont("Arial", 20)

		name_surface = font.render(self.__player_1_name, True, (0, 0, 0))
		name_rect = name_surface.get_rect()
		name_rect.center = (
			int(PLAYER_INFO_X + INFO_WIDTH / 2), int(PLAYER_1_INFO_Y + INFO_HEIGHT / 2))
		self.__display.blit(name_surface, name_rect)

		name_surface = font.render(self.__player_2_name, True, (0, 0, 0))
		name_rect = name_surface.get_rect()
		name_rect.center = (
			int(PLAYER_INFO_X + INFO_WIDTH / 2), int(PLAYER_2_INFO_Y + INFO_HEIGHT / 2))
		self.__display.blit(name_surface, name_rect)

		font = pygame.font.Font(None, 32)

		end_game_text = "Exit game"
		pygame.draw.rect(self.__display, "black", (37, GUI_HEIGHT - 100, 127, 32), 0, 10)
		end_game_surface = font.render(end_game_text, True, "white")
		self.__display.blit(end_game_surface, (48, GUI_HEIGHT - 95))

	def game(self):
		"""
			Handles the game
		"""

		self.set_player_names()

		self.__display.blit(self.__board, (200, 0))
		self.display_names(self.__curr_player)

		pygame.display.update()

		end_game_button = pygame.draw.rect(self.__display, "black", (37, GUI_HEIGHT - 100, 127, 32), 0, 10)

		while True:
			while not self.__winner:
				if not self.__ai_choice:
					row, col = self.click_pos(end_game_button)
				else:
					if self.__curr_player == 2:
						row = randint(0, 18)
						col = randint(0, 18)
					else:
						row, col = self.click_pos(end_game_button)
				while not self.__game.val_pos((row, col), 0):
					if not self.__ai_choice:
						row, col = self.click_pos(end_game_button)
					else:
						if self.__curr_player == 2:
							row = randint(0, 18)
							col = randint(0, 18)
						else:
							row, col = self.click_pos(end_game_button)

				self.__board_game[row, col] = self.__curr_player
				self.__winner = self.__game.check_winner(self.__curr_player, 0)
				if self.__curr_player == 1:
					winner_name = self.__player_1_name
				else:
					winner_name = self.__player_2_name
				self.pos_piece((row, col), self.__curr_player)

				self.__curr_player = 3 - self.__curr_player

				winner_font = pygame.font.SysFont("Arial", 50)

				if self.__winner != 0:
					text = winner_name + " has won the game!"
					winner_surface = winner_font.render(text, True, "white")
					winner_rect = winner_surface.get_rect()
					winner_rect.center = (int(GUI_WIDTH / 2), int(GUI_HEIGHT / 2))
					pygame.draw.rect(self.__display, "black", (int((GUI_WIDTH / 2) - 337), 220, 675, 260), 0, 25)
					self.__display.blit(winner_surface, winner_rect)
				else:
					self.display_names(self.__curr_player)

				pygame.display.update()
				self.__rate.tick(TICKS)

				if self.__winner != 0:
					pygame.time.delay(2500)
					gui = GUI(self.__ai_choice)
					gui.start()

	def pos_piece(self, pos, player):
		"""
			Sets the piece on a specified position

			:param pos: Position
			:param player: Current player
		"""

		x = 208 + pos[1] * 36.5
		y = pos[0] * 36.5 + 8

		if player == PLAYER_1:
			self.__display.blit(self.__black, (x, y))
		else:
			self.__display.blit(self.__white, (x, y))

	@staticmethod
	def click_pos(end=None):
		"""
			Returns the row and column of the clicked position on the board

			:param end: Exit game button
			:return: Row and column of the clicked position on the board
		"""

		while True:
			for e in pygame.event.get():
				if e.type == MOUSEBUTTONDOWN:
					if end.collidepoint(e.pos):
						pygame.quit()
						sys.exit()
				if e.type == QUIT:
					pygame.quit()
					sys.exit()
				elif e.type == MOUSEBUTTONUP:
					x, y = pygame.mouse.get_pos()
					row = int(round((y - 20) / 36.5))
					col = int(round((x - 220) / 36.5))
					return row, col

	def input(self, player, typ):
		"""
			Allows each player to input their name

			:param player: Player name
			:param typ: Player number (1/2)
		"""

		color_active = "black"

		color_passive = "white"
		color = color_passive

		active = False

		input_rect = pygame.draw.rect(self.__display, "white", (GUI_WIDTH / 2 - 121, 200, 250, 32), 0, 25)
		end_game_button = pygame.draw.rect(self.__display, "black", (GUI_WIDTH / 2 - 121, GUI_HEIGHT - 100, 250, 32))

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if end_game_button.collidepoint(event.pos):
						pygame.quit()
						sys.exit()
					if input_rect.collidepoint(event.pos):
						active = True
					else:
						active = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_BACKSPACE:
						player = player[:-1]
					elif event.key == pygame.K_RETURN:
						return player
					else:
						player += event.unicode

			self.__display.fill((255, 255, 255))

			if active:
				color = color_active
				border = color_passive
			else:
				color = color_passive
				border = color_active

			if typ == 1:
				label = "Enter player 1 name"
			else:
				label = "Enter player 2 name"

			font = pygame.font.Font(None, 32)

			end_game_text = "Exit game"
			pygame.draw.rect(self.__display, "black", (GUI_WIDTH / 2 - 58, GUI_HEIGHT - 100, 135, 32), 0, 10)
			end_game_surface = font.render(end_game_text, True, "white")
			self.__display.blit(end_game_surface, (end_game_button.x + 78, end_game_button.y + 5))

			name_surface = font.render(label, True, "black")
			name_rect = name_surface.get_rect()
			name_rect.center = (GUI_WIDTH / 2 + 4, 150)
			self.__display.blit(name_surface, name_rect)

			pygame.draw.rect(self.__display, color, (GUI_WIDTH / 2 - 121, 200, 250, 32), 0, 10)
			text_surface = font.render(player, True, border)
			self.__display.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

			pygame.draw.rect(self.__display, border, (GUI_WIDTH / 2 - 121, 200, 250, 32), 2, 2)
			text_surface_border = font.render(player, True, (0, 0, 0))
			self.__display.blit(text_surface_border, (input_rect.x + 5, input_rect.y + 5))

			pygame.draw.rect(self.__display, color, (GUI_WIDTH / 2 - 121, 200, 250, 32), 0, 10)
			text_surface = font.render(player, True, border)
			self.__display.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

			pygame.display.flip()
			self.__rate.tick(TICKS)

	def set_player_names(self):
		"""
			Sets both players' names
		"""

		if self.__player_1_name == "":
			self.__player_1_name = self.input(self.__player_1_name, 1)
			if not self.__ai_choice:
				self.__player_2_name = self.input(self.__player_2_name, 2)
		else:
			self.__player_1_name = ""
			if not self.__ai_choice:
				self.__player_2_name = ""
			self.__player_1_name = self.input(self.__player_1_name, 1)
			if not self.__ai_choice:
				self.__player_2_name = self.input(self.__player_2_name, 2)

	def start(self):
		"""
			Starts the game
		"""

		self.game()

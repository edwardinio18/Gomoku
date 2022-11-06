"""
	Settings
"""

from configparser import ConfigParser

from src.gui.gui import GUI
from src.ui.ui import UI


class Settings:
	"""
		Settings class
	"""

	def __init__(self):
		"""
			Initializes the settings class
		"""

		self.__ui = None
		self.__ai = False

		parser = ConfigParser()
		parser.read("../../settings.properties")

		if parser.get("options", "ai") == "True":
			self.__ai = True

		if parser.get("options", "ui") == "ui":
			self.__ui = UI(self.__ai)
		else:
			self.__ui = GUI(self.__ai)

	def start(self):
		"""
			Start the application with selected UI type
		"""

		self.__ui.start()

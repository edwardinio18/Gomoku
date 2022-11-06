"""
	Main
"""

from src.settings.settings import Settings


class Main:
	"""
		Main class
	"""

	def __init__(self):
		"""
			Initializes the main class
		"""

		self.__settings = Settings()

	def start(self):
		"""
			Starts the program
		"""

		self.__settings.start()


main = Main()
main.start()

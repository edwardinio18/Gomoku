"""
	AI
"""

from random import randint


class AI:
	"""
		AI class
	"""

	def __init__(self):
		"""
			Initializes the AI class
		"""

		self._name = ""

	def rand_name(self):
		"""
			Generates a random name for the AI
		"""

		names = ["Liam", "Noah", "Oliver", "Elijah", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander",
		         "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Logan", "Jackson", "Levi", "Sebastian", "Mateo",
		         "Jack", "Owen", "Theodore", "Aiden", "Samuel", "Joseph", "John", "David", "Wyatt", "Matthew",
		         "Luke",
		         "Asher", "Carter", "Julian", "Grayson", "Leo", "Jayden", "Gabriel", "Isaac", "Lincoln", "Anthony",
		         "Hudson", "Dylan", "Ezra", "Thomas", "Charles", "Christopher", "Jaxon", "Maverick", "Josiah",
		         "Isaiah",
		         "Andrew", "Elias", "Joshua", "Nathan", "Caleb", "Ryan", "Adrian", "Miles", "Eli", "Nolan",
		         "Christian",
		         "Aaron", "Cameron", "Ezekiel", "Colton", "Luca", "Landon", "Hunter", "Jonathan", "Santiago",
		         "Axel",
		         "Easton", "Cooper", "Jeremiah", "Angel", "Roman", "Connor", "Jameson", "Robert", "Greyson",
		         "Jordan",
		         "Ian", "Carson", "Jaxson", "Leonardo", "Nicholas", "Dominic", "Austin", "Everett", "Brooks",
		         "Xavier",
		         "Kai", "Jose", "Parker", "Adam", "Jace", "Wesley", "Kayden", "Silas", "Bennett", "Declan",
		         "Waylon",
		         "Weston", "Evan", "Emmett", "Micah", "Ryder", "Beau", "Damian", "Brayden", "Gael", "Rowan",
		         "Harrison",
		         "Bryson", "Sawyer", "Amir", "Kingston", "Jason", "Giovanni", "Vincent", "Ayden", "Chase", "Myles",
		         "Diego", "Nathaniel", "Legend", "Jonah", "River", "Tyler", "Cole", "Braxton", "George", "Milo",
		         "Zachary", "Ashton", "Luis", "Jasper", "Kaiden", "Adriel", "Gavin", "Bentley", "Calvin", "Zion",
		         "Juan", "Maxwell", "Max", "Ryker", "Carlos", "Emmanuel", "Jayce", "Lorenzo", "Ivan", "Jude",
		         "August",
		         "Kevin", "Malachi", "Elliott", "Rhett", "Archer", "Karter", "Arthur", "Luka", "Elliot", "Thiago",
		         "Brandon", "Camden", "Justin", "Jesus", "Maddox", "King", "Theo", "Enzo", "Matteo", "Emiliano",
		         "Dean",
		         "Hayden", "Finn", "Brody", "Antonio", "Abel", "Alex", "Tristan", "Graham", "Zayden", "Judah",
		         "Xander",
		         "Miguel", "Atlas", "Messiah", "Barrett", "Tucker", "Timothy", "Alan", "Edward", "Leon", "Dawson",
		         "Eric", "Ace", "Victor", "Abraham", "Nicolas", "Jesse"]

		self._name = names[randint(0, len(names) - 1)]
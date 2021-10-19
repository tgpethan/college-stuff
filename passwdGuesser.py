# ==========- Password Guessing Game -========= #
#      Created by Holly Stubbs (tgpethan)       #
#     Licensed under MIT (Check repo root)      #
#   https://github.com/tgpethan/college-stuff   #
# ============================================= #

# Constants
PASSWORDER_NAME:str = "Anna"
MAX_ATTEMPTS:int = 8

# Functions
def clearScreen():
	# Use a lot of empty lines to "clear" the screen
	#  - Why did I do this? Because python has no built in
	#    way to clear the console, that's why. >:(
	for i in range(100):
		print("")

def gameRun():
	passwd = input("Enter your password {0}! : ".format(PASSWORDER_NAME))

	# ""Clear"" screen so guesser can't see the password
	clearScreen()

	guesserName = input("Enter your name guesser: ")

	print("Welcome to the Password Guessing Game {0}!\nYou have {1} attempts to guess my password. Good Luck!".format(guesserName, MAX_ATTEMPTS))

	# Default to false, we only change this is the guesser
	# guesses the password
	correctGuess = False

	# Ask for a password guess the number of times defined in MAX_ATTEMPTS
	for i in range(MAX_ATTEMPTS):
		passwdGuess = input("Enter your guess: ")
		if passwdGuess == passwd:
			print("Well done! It took you {0} attempts to guess my password!".format(i + 1))
			correctGuess = True
			break
		else:
			print("Try again")
	
	# If the user did not guess the password in MAX_ATTEMPTS then
	# we tell them the password
	if not correctGuess:
		print("Ouch! Looks like you couldn't guess the password.\nThe correct password was \"{0}\"".format(passwd))

	choice = input("Play again? (y/n) ")
	if choice == "y":
		clearScreen()
		# Run the game again
		gameRun()

# Start the game
gameRun()

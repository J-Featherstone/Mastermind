import sys, pygame, random

colours = ["black", "white", "blue", "green", "yellow", "red"]
colours_str = ", ".join(colours)
	

#generates a hard pattern for mastermind (six colours, duplicates, five slots)
def generate_pattern_hard():
	pattern = []
	for x in range(0, 5):
		pattern.append(colours[random.randint(0, 5)])
		
	return pattern

#returns "pins", "black" if the correct colour in correct place, "white if correct colour in wrong place"
def check_guess(answer1, guess1):
	answer = []
	guess = []
	for c in answer1:
		answer.append(c)
	for c in guess1:
		guess.append(c)
		
	pins = []
	
	for ind, clr in enumerate(guess):
		if guess[ind] == answer[ind]:
			pins.append("black")
			guess[ind] = "checked"
			answer[ind] = "checked"
	
	for ind, clr in enumerate(answer):
		if clr != "checked":
			for ind2, clr2 in enumerate(guess):
				if clr2 == clr:
					pins.append("white")
					answer[ind] = "checked"
					guess[ind2] = "checked"
	
	answer = []
	guess = []
	for c in answer1:
		answer.append(c)
	for c in guess1:
		guess.append(c)				
	return pins

#asks user to guess the answer by typing colours, asks for valid inputs if not given	
def input_guess(answer):
	guess = []
	for l in answer:
		inp = input("input colour: ")
		while inp not in colours:
			inp = input("please type " + colours_str + ": ")
		guess.append(inp)
		
	return guess


#actual game loop
'''print("Welcome to mastermind, you will be asked to guess my sequence of 5 colours from: " + colours_str + " you have unlimited guesses.")

pattern = generate_pattern_hard()

pins = []
guess = []

while pins != ["black", "black", "black", "black", "black"]:
	guess = input_guess(pattern)
	pins = check_guess(pattern, guess)
	print(guess)
	print(pins)
	
print("congratulations you win!")'''

#bug somwhere where not enough pins get returned from a guess sometimes.

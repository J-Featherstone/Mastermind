import random

colours = ["black", "white", "blue", "green", "yellow", "red"]

#generates a hard pattern for mastermind (six colours, duplicates, five slots)
def generate_pattern_hard():
	pattern = []
	for x in range(0, 5):
		pattern.append(colours[random.randint(0, 5)])
		
	return pattern

#returns "pins", "black" if the correct colour in correct place, "white if correct colour in wrong place"
def check_guess(answer, guess):

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
					
	return pins
	
def guess_input(answer):
	guess = []
	for l in answer:
		inp = input("input colour: ")
		guess.append(inp)
	return guess

print(guess_input(["black", "green", "red", "blue", "red"]))


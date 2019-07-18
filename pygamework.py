import mastermind
import pygame, sys
pygame.init()

colour_dic = {"black": (0, 0, 0), "white": (255, 255, 255), "blue": (0, 0, 255), "green": (0, 255, 0), "yellow": (255, 255, 0), "red": (255, 0, 0)}
current_guess = []
current_pins = []
old_guess = []
old_pins = []
difficulty = 5
guess = False

size = width, height = 500, 800

#row is an integer 0 - max guesses
def draw_colour_pins(row, pins):
	y = 800 - (row * 50) - 25
	for ind, c in enumerate(pins):
		x = ind * 50 + 25
		pygame.draw.circle(screen, colour_dic[c], (x, y), 20)

def present_colours():
		x = 475
		count = 0
		for c, num in colour_dic.items():
			pygame.draw.circle(screen, num, (x, count * 50 + 25), 20)
			count += 1

def buttons(current_guess, current_pins, old_pins, old_guess, pattern):
	for evento in pygame.event.get():
		if evento.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			if 495 > mouse[0] > 455 and len(colour_dic) * 50 + 45 > mouse[1] > 0:
				#while len(current_guess) < difficulty:
				colour_ind = int(mouse[1] / 50)
				#print(colour_ind)
				colour_pix = screen.get_at(mouse)
				#print(colour_pix)
				colour_name = ""
				for colo, num in colour_dic.items():
					if num == colour_pix:
						colour_name = colo
				#print(colour_name)
				if colour_name != "":
					if "empty" in current_guess:
						for k, c in enumerate(current_guess):
							if c == "empty":
								current_guess[k] = colour_name
								break
					elif len(current_guess) < difficulty:			
						current_guess.append(colour_name)
						colour_name = ""
				else:
					break
				#print(current_guess)
				#pygame.draw.circle(screen, colour_pix, (len(current_guess) * 50 + 50, 50), 20)
				draw_current_guess(current_guess)
				pygame.display.update()
			
			elif 150 < mouse[0] < 450 and 730 - (len(old_guess) * 50)  < mouse[1] <  740 - (len(old_guess) * 50):
				colour_pix = screen.get_at(mouse)
				#print(colour_pix)
				colour_name = ""
				for colo, num in colour_dic.items():
					if num == colour_pix:
						colour_name = colo
				if colour_name != "":
					guess_ind = int((mouse[0] - 130) / 50)
					current_guess[guess_ind] = "empty"
				else:
					break
				print(current_guess)
				draw_current_guess(current_guess)
				pygame.display.update()
				
			elif 400 < mouse[0] < 490 and 740 < mouse[1] < 790:
				if screen.get_at(mouse) == (0, 255, 0):
					print(current_guess)
					old_guess.append(current_guess)
					current_guess = []
					current_pins = mastermind.check_guess(pattern, current_guess)
					print(current_pins)
					old_pins.append(current_pins)
					current_pins = []
					draw_old(old_guess, old_pins)
					print(old_guess)
					print(old_pins)
					#print(current_guess)
					pygame.display.update()
				
		
def draw_current_guess(current_guess):
	for k, colour in enumerate(current_guess):
		if colour in colour_dic:
			col_num = colour_dic.get(colour)
			pygame.draw.circle(screen, col_num, (k * 50 + 150, height - 50 - (len(old_guess) * 50)), 20)
		elif colour == "empty":
				pygame.draw.circle(screen, (255, 0, 255), (k * 50 + 150, height - 50 - (len(old_guess) * 50)), 20)


def draw_old(old_guess, old_pins):
	for l, guess in enumerate(old_guess):
		for s, col in enumerate(guess):
			col_num = colour_dic.get(col)
			pygame.draw.circle(screen, col_num, (s * 50 + 150, height - 50 - (l * 50)), 20)
			
	for l, pins in enumerate(old_pins):
		for k, colour in enumerate(pins):	
			col_num = colour_dic.get(colour)
			pygame.draw.circle(screen, col_num, (k * 25 + 10, height - 50 -(l * 50)), 10)
	

def undoer():
	for evento in pygame.event.get():
		if evento.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			if 200 < mouse[0] < 450 and 0 < mouse[1] <  50:
				colour_pix = screen.get_at(mouse)
				print(colour_pix)
			else:
				break
			

screen = pygame.display.set_mode(size)

screen.fill((255, 0, 255))
pygame.display.update()
#draw_colour_pins(1, ("green", "green", "red", "blue", "green"))
#draw_colour_pins(2, ("green", "yellow", "red", "blue", "green", "black", "red", "white"))
present_colours()
pygame.display.update()

#clock.tick(15)

#pygame.display.flip()

pattern = mastermind.generate_pattern_hard()
print(pattern)	

while (1):

	#print(pattern)

	while guess == False:
		if len(current_guess) == difficulty and "empty" not in current_guess:
			pygame.draw.rect(screen, (0, 255, 0), (400, 740, 90, 50))
			buttons(current_guess, current_pins, old_pins, old_guess, pattern)
		else:
			pygame.draw.rect(screen, (255, 0, 0), (400, 740, 90, 50))			
		buttons(current_guess, current_pins, old_pins, old_guess, pattern)
		
	
	
	#pygame.display.flip()
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

#click a colour on right to make it appear on left


#def draw_pins(pins):

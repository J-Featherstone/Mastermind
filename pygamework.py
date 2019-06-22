import pygame, sys
pygame.init()

colour_dic = {"black": (0, 0, 0), "white": (255, 255, 255), "blue": (0, 0, 255), "green": (0, 255, 0), "yellow": (255, 255, 0), "red": (255, 0, 0)}
current_guess = []
old_guess = []
old_pins = []

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

def buttons():
	for evento in pygame.event.get():
		if evento.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			if 495 > mouse[0] > 455 and len(colour_dic) * 50 + 45 > mouse[1] > 0:
				while len(current_guess) < 5:
					colour_ind = int(mouse[1] / 50)
#get the nth colour in colour_dic and add it to current_guess. print current guess
		

screen = pygame.display.set_mode(size)

screen.fill((255, 0, 255))
pygame.display.update()
#draw_colour_pins(1, ("green", "green", "red", "blue", "green"))
#draw_colour_pins(2, ("green", "yellow", "red", "blue", "green", "black", "red", "white"))
present_colours()
pygame.display.update()

#clock.tick(15)

#pygame.display.flip()

	

while (1):
	for evento in pygame.event.get():
			#print(evento);
		if evento.type == pygame.MOUSEBUTTONDOWN:
			mouse = pygame.mouse.get_pos()
			#if pygame.mouse.get_pos() >= (150,230):
			if 450 + 50 > mouse[0] > 450 and 25 + 50 > mouse[1] > 25:
				pygame.draw.circle(screen, (0, 0, 0), (50, 50), 20)
				pygame.display.update()
	#pygame.display.flip()
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

#click a colour on right to make it appear on left


#def draw_pins(pins):

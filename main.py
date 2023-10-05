from bezier4 import bezier4
import sys, pygame
pygame.init()

size = width, height = 500, 500
black = 0, 0, 0
white = 255, 255, 255
purple = 255, 17, 168

screen = pygame.display.set_mode(size,pygame.RESIZABLE)

control_points = []
state = "SETTING"
pressedCP = None


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			if state=="SETTING":
				control_points.append(pygame.mouse.get_pos())
			pressedCP = None
		if pressedCP != None:
			bez.control_points[pressedCP] = pygame.mouse.get_pos()

	screen.fill(black)

	if state == "SETTING":
		if len(control_points) == 5:
				bez = bezier4(control_points, 100)
				state = "BEZIER"
				control_points = []			

		for cp in control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)

	elif state == "BEZIER":
		if (pygame.mouse.get_pressed() == (True, False, False)):
			x1,y1 = pygame.mouse.get_pos()
			for i in range(5):
				x,y = bez.control_points[i]
				if(abs(x-x1)<=10 and abs(y-y1)<=10):
					pressedCP = i
					# bez.control_points[i] = (x1,y1)
			bez.function()

		tani = bez.control_points[-1]
		tanf = bez.control_points[-2]
		# # mult = [(tani[0]-tanf[0])/(tani[1]-tanf[1]), (tani[1]-tanf[1])/(tani[0]-tanf[0])]
		tanf = (0.5*tanf[0] + 0.5*tani[0], 0.5*tanf[1] +0.5*tani[1])

		pygame.draw.lines(screen, purple, False, bez.points, 2)
		pygame.draw.line(screen,(255,255,0),tani,tanf,2)
		for cp in bez.control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)

	pygame.display.flip()



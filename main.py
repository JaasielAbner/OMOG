from bezier4 import bezier4
from nurbs4 import NURBSCurve
import sys, pygame
pygame.init()

control_points = []

knots = [0, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4]

size = width, height = 500, 500
black = 0, 0, 0
white = 255, 255, 255
purple = 255, 17, 168
green = 17, 200, 63

da,db = 0,0

screen = pygame.display.set_mode(size,pygame.RESIZABLE)

control_points = []
state = "SETTING"
pressedCP = None
witch = None

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			if state!="BEZIER":
				control_points.append(pygame.mouse.get_pos())
			pressedCP = None
			witch = None
		if pressedCP != None:
			if witch == "bez":
				bez.control_points[pressedCP] = pygame.mouse.get_pos()
			elif witch == "nur":
				curve.control_points[pressedCP] = pygame.mouse.get_pos()

	screen.fill(black)

	if state == "SETTING":
		if len(control_points) == 5:
				bez = bezier4(control_points, 100)
				state = "NURBS"
				control_points = []			

		for cp in control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)

	elif state == "NURBS":
		if len(control_points) == 5:
				curve = NURBSCurve(control_points, knots, 100)
				state = "BEZIER"
				control_points = []			

		for cp in control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)
		
		pygame.draw.lines(screen, purple, False, bez.points, 2)
		for cp in bez.control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)

	elif state == "BEZIER":
		if (pygame.mouse.get_pressed() == (True, False, False)):
			x1,y1 = pygame.mouse.get_pos()
			for i in range(5):
				x,y = bez.control_points[i]
				if(abs(x-x1)<=10 and abs(y-y1)<=10):
					pressedCP = i
					witch = "bez"
			for i in range(1,5):
				x,y = curve.control_points[i]
				if(abs(x-x1)<=10 and abs(y-y1)<=10):
					pressedCP = i
					witch = "nur"
		da = (bez.control_points[-1][0] - curve.control_points[0][0])
		db = (bez.control_points[-1][1] - curve.control_points[0][1])
		if (da + curve.diff[0] != 0) and (db + curve.diff[1]!= 0):
			curve.update(da,db)
		else:
			dela = bez.control_points[-1][0] - (curve.control_points[1][0] - bez.control_points[-1][0])
			delb = bez.control_points[-1][1] - (curve.control_points[1][1] - bez.control_points[-1][1])
			bez.control_points[-2] = (dela,delb)
		bez.function()
		curve.function()


		# # mult = [(tani[0]-tanf[0])/(tani[1]-tanf[1]), (tani[1]-tanf[1])/(tani[0]-tanf[0])]
		pygame.draw.lines(screen, purple, False, bez.points, 2)
		pygame.draw.lines(screen, green, False, curve.points, 2)
		for cp in bez.control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)
		for cp in curve.control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)

	pygame.display.flip()



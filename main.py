from bezier4 import bezier4
from nurbs4 import NURBSCurve
import sys, pygame
pygame.init()

# Define control points as a list of lists
control_points = [
    [300, 300],
    [100, 100],
    [200, 200],
    [300, 200],
    [400, 500]
]

# Define the knot vector. For a degree 4 curve with 5 control points, you need 5 + 4 + 2 = 11 knots.
knots = [0, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4]

# Create an instance of the NURBSCurve class
curve = NURBSCurve(control_points, knots)

nurbs = []

for i in range(90):
	a = i/26
	p = curve.evaluate(a)
	nurbs.append((p[0],p[1]))


size = width, height = 500, 500
black = 0, 0, 0
white = 255, 255, 255
purple = 255, 17, 168
green = 17, 200, 63

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
			bez.function()
			curve = NURBSCurve(bez.control_points, knots)
			nurbs = []
			for i in range(100):
				a = i/100
				p = curve.evaluate(a)
				nurbs.append((p[0],p[1]))

		# # mult = [(tani[0]-tanf[0])/(tani[1]-tanf[1]), (tani[1]-tanf[1])/(tani[0]-tanf[0])]
		pygame.draw.lines(screen, purple, False, bez.points, 2)
		pygame.draw.lines(screen, green, False, nurbs, 2)
		for cp in bez.control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)
		for cp in curve.control_points:
			pygame.draw.circle(screen, white, cp, 5, 2)

	pygame.display.flip()



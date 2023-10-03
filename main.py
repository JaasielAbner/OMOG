from bezier4 import bezier4
import sys, pygame
pygame.init()

size = width, height = 300, 300
black = 0, 0, 0

screen = pygame.display.set_mode(size)

control_points = [(10,10),(10,115),(125,200),(230,178)]
bez = bezier4(control_points, 5000)
pointList = bez.get_points()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	screen.fill(black)
	startPos = pointList[0]
	for cp in control_points:
		pygame.draw.circle(screen,(150,17,255),cp,5,1)

	for endPos in pointList[1:]:
		pygame.draw.line(color=(255,255,255),surface=screen,start_pos=startPos,end_pos=endPos)
		startPos = endPos
	pygame.display.flip()



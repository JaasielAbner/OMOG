import sys, pygame


def bezierFour(cPs,p):
    points = []
    for i in range(p+1):
        t = i/p
        x = pow((1-t),4) * cPs[0][0] + t * pow((1-t),3) * cPs[1][0] * 4 + pow(t,2) * pow((1-t),2) * cPs[2][0] * 6 + pow(t,3) * pow((1-t),1) * cPs[3][0] * 4 + pow(t,4) * cPs[4][0] 
        y = pow((1-t),4) * cPs[0][1] + t * pow((1-t),3) * cPs[1][1] * 4 + pow(t,2) * pow((1-t),2) * cPs[2][1] * 6 + pow(t,3) * pow((1-t),1) * cPs[3][1] * 4 + pow(t,4) * cPs[4][1] 
        points.append((x,y))
    return points


pygame.init()

size = width, height = 1000, 1000
black = 0, 0, 0
white = 255, 255, 255
purple = 255, 17, 168

controlPoints = [(400,300),(500,200),(700,300),(700,600),(400,900)]

screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if (pygame.mouse.get_pressed() == (True, False, False)):
        x1,y1 = pygame.mouse.get_pos()
        for i in range(5):
            x,y = controlPoints[i]
            if(abs(x-x1)<=10 and abs(y-y1)<=10):
                controlPoints[i] = (x1,y1)

    screen.fill(black)
    pygame.draw.lines(screen, purple, False, bezierFour(controlPoints,5), 2)
    for cp in controlPoints:
        pygame.draw.circle(screen, white, cp, 5, 2)
    pygame.display.flip()



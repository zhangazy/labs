import pygame
import time
import math
pygame.init()
PI = math.pi

#colors RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


#size of screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
SURFACE_WIDTH=640
SURFACE_HEIGHT=480
WINDOW_CENTER = SURFACE_HEIGHT/2


#FPS
FPS = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("sin x and cos x")
clock = pygame.time.Clock()

#fonts
font1 = pygame.font.SysFont("Calibri", 17)
font2 = pygame.font.SysFont("Calibri", 14)
font3 = pygame.font.SysFont("Calibri", 14,3)


#x points and y points
y_points = (-1.00 ,-0.75 ,-0.50 ,-0.25 ,0.00 ,0.25 ,0.50 ,0.75 ,1.00)
x1_points = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
x2_points = ['', '_ ', '', '_ ', '', '_ _', '', '   _', '', '   ', '', '   ', '']
x3_points = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']



showSine = True
showCosine = True
pause = False
xPos = 80
AMPLITUDE = 160
step = 0
posRecord = {'sin': [], 'cos': []}
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(WHITE)   
    #graph lines
    pygame.draw.line(screen,BLACK,(50,50),(705,50),3)
    pygame.draw.line(screen,BLACK,(50,430),(705,430),3)
    pygame.draw.line(screen,BLACK,(50,50),(50,430),3)
    pygame.draw.line(screen,BLACK,(380,50),(380,430),3)
    pygame.draw.line(screen,BLACK,(705,50),(705,430),3)
    pygame.draw.line(screen,BLACK,(50,240),(705,240),3)



    #cos and sin colors
    screen.blit(font3.render('sin(x)', False, BLACK), (750, 225))
    screen.blit(font3.render('cos(x)', False, BLACK), (750, 245))
    pygame.draw.line(screen, RED, (720, 233), (740, 233))
    pygame.draw.line(screen, BLUE, (720, 253), (740, 253))
    for x in range(7):
        pygame.draw.line(screen, BLACK, (x*100+80, 50), (x*100+80, 430))
    # x coordinates
    for x in range(80, 700, 50):
        screen.blit(font1.render(x1_points[(x - 80) // 50], False, BLACK), (x - 10, 450))
        screen.blit(font1.render(x2_points[(x - 80) // 50], False, BLACK), (x - 20, 450))
        screen.blit(font1.render(x3_points[(x - 80) // 50], False, BLACK), (x - 10, 475))
    # y coordinates
    for y in y_points:
        text =font1.render(str(y),True,BLACK)
        screen.blit(text,(5,-y*160+240))
        pygame.draw.line(screen,BLACK,(50,-y*160+240),(705,-y*160+240))
    
    #sin
    yPos = -1 * math.sin(step) * AMPLITUDE
    posRecord['sin'].append((int(xPos), int(yPos) + WINDOW_CENTER))
    #cos
    yPos = -1 * math.cos(step) * AMPLITUDE
    posRecord['cos'].append((int(xPos), int(yPos) + WINDOW_CENTER))
    if showSine:
        for x, y in posRecord['sin']:
            pygame.draw.circle(screen, RED, (x, y), 2)
    if showCosine:
        for x, y in posRecord['cos']:
            pygame.draw.circle(screen, BLUE, (x, y), 2)
    pygame.display.update()
    clock.tick(FPS)
    if not pause:
        xPos += 0.385
        if xPos > SURFACE_WIDTH+40:
            xPos = 80
            posRecord = {'sin': [], 'cos': []}
            step = 0
        else:
            step += 0.008
            step %= 2 * PI
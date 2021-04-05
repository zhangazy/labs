import pygame
pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCREEN_WIDHT, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption("Cos and sin graph")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(WHITE)
    

    pygame.display.flip()
pygame.quit()



            
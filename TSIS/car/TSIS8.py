import pygame, sys
from pygame.locals import *
import random
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
WHITE = (255,255,255)
BLACK = (0, 0 , 0)
BLUE = (0, 0, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
SCREEN_WIDTH, SCREEN_HEIGHT = 400,600
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW.fill(WHITE)
pygame.display.set_caption("TSIS 8")
class enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.surf = pygame.Surface((50,80))
        self.rect = self.surf.get_rect(center = (random.randint(40, 360), 0))

    def move(self):
            self.rect.move_ip(0,10)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(30, 370), 0)
        
    def draw(self, surface):
            surface.blit(self.image, self.rect)

class player(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect()
    
    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
P1 = player()
E1 = enemy()
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()
    WINDOW.fill(WHITE)
    P1.draw(WINDOW)
    E1.draw(WINDOW)
    pygame.display.flip()
    pygame.display.update()
    FramePerSec.tick(FPS)
pygame.quit()
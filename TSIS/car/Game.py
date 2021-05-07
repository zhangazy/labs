#Imports
import pygame, sys
import random, time
from pygame.locals import *

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)

#Other Variables for use in the program
WIDTH = 400
HEIGHT = 600
SPEED = 5
SCORE = 0

DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car game")

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
fontsmall = pygame.font.SysFont("Verdana", 20)
gameover = font.render("Crashed", True, RED)
background = pygame.image.load("AnimatedStreets.jpg")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(80,WIDTH-80)
                                                 , 0))
        
      def move(self):
        global SPEED
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_r]:
            SPEED = random.randint(5, 10)
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(80, WIDTH - 80), 0)
        

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('coin.png')
        self.surf = pygame.Surface((10,10))
        self.rect = self.surf.get_rect(center = (random.randint(80,WIDTH-80), 0))
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(80, WIDTH - 80), 0)
        elif pygame.sprite.spritecollideany(P1,coins):
            pygame.mixer.Sound('coin.mp3').play()
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(80, WIDTH - 80), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop

while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.1      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = fontsmall.render(str(SCORE), True, BLACK)
    
    DISPLAYSURF.blit(scores, (360,10))
    myfont = pygame.font.SysFont("Arial", 24)
    myfont2 = pygame.font.SysFont("Arial", 15)
    result = myfont.render('Your score is: ', True, YELLOW)
    rescore = myfont.render(str(SCORE), True, YELLOW)
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    #To be run if collision occurs between Player and Enemy
    
    
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(1)
          DISPLAYSURF.fill(BLUE)
          DISPLAYSURF.blit(gameover, (70,250))
          DISPLAYSURF.blit(result, (130, 230))
          DISPLAYSURF.blit(rescore, (260, 230))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(7)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
    


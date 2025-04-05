import pygame
import random
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 576
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("racer task")
icon = pygame.image.load('lab8/images/isaac icon.png').convert_alpha()
pygame.display.set_icon(icon)
FPS = pygame.time.Clock()

# background
background = pygame.image.load('lab8/images/isaac background.jpg').convert()
background_y = 0

# OST
background_sound = pygame.mixer.Sound('lab8/sounds/Machine in the Walls (Mausoleum).mp3')
background_sound.play(-1)

# enemy and coin speed
speed = 10

# class for player
class isaac(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.walk_up = [
            pygame.image.load('lab8/images/isaac movement/isaac-up-1.png').convert_alpha(),
            pygame.image.load('lab8/images/isaac movement/isaac-up-2.png').convert_alpha(),
            pygame.image.load('lab8/images/isaac movement/isaac-up-3.png').convert_alpha(),
            pygame.image.load('lab8/images/isaac movement/isaac-up-4.png').convert_alpha()
        ]
        self.image = self.walk_up[0]
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 4 / 5))
        self.anim_count = 0
        self.speed_left_right = 18
        self.speed_down = 11
        self.speed_up = 22

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 33:
            self.rect.x -= self.speed_left_right
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH - 33:
            self.rect.x += self.speed_left_right
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT - 10:
            self.rect.y += self.speed_down
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed_up

    def draw(self, surface):
        surface.blit(self.walk_up[self.anim_count], (self.rect.x, self.rect.y))
        self.anim_count += 1
        if self.anim_count >= len(self.walk_up):
            self.anim_count = 0

# class for enemies  
class enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.enemy_list = [
            pygame.image.load('lab8/images/Spikes.png').convert_alpha(),
            pygame.image.load('lab8/images/Spiked_Rock.png').convert_alpha(),
            pygame.image.load('lab8/images/RedPoop.png').convert_alpha()
        ]
        self.enemy_image = random.choice(self.enemy_list)
        self.rect = self.enemy_image.get_rect()
        self.rect.center = (random.randint(33, SCREEN_WIDTH - 33), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(33, SCREEN_WIDTH - 33), 0)

    def draw(self, surface):
        surface.blit(self.enemy_image, self.rect)

class coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load('lab8/images/coins/isaac penny.gif').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speed = 10

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

font = pygame.font.SysFont('Verdana', 30)

PLAYER = isaac()
ENEMIES = enemy(speed)
COIN = coin(speed)

cnt = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False 
          pygame.quit()
          sys.exit()

    # background movement
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - SCREEN_HEIGHT))

    background_y += 10
    if background_y >= SCREEN_HEIGHT:
        background_y = 0

    PLAYER.move()
    ENEMIES.move()
    COIN.move()


    if PLAYER.rect.colliderect(COIN.rect):
        cnt += 1 
        COIN.reset_position()

    if PLAYER.rect.colliderect(ENEMIES.rect):
        pygame.quit()
        sys.exit()

    PLAYER.draw(screen)
    ENEMIES.draw(screen)
    COIN.draw(screen)

    counter = font.render(str(cnt), True, (255, 255, 255))
    screen.blit(counter, (SCREEN_WIDTH - 50, 10))

    

    pygame.display.update()

    FPS.tick(20)
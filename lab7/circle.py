import pygame

pygame.init()

# setting window size
screen_length = 1200
screen_width = 600

# creating a window
screen = pygame.display.set_mode((screen_length, screen_width))
pygame.display.set_caption("Circle Task")

# setting icon
icon = pygame.image.load('lab7/images/dark souls sun.png')
pygame.display.set_icon(icon)

# creating a circle
character = pygame.image.load('lab7/images/dark souls sun.png')
character_speed = 20
character_x = screen_length / 2 - 50
character_y = screen_width / 2 - 50

# controll FPS
FPS = pygame.time.Clock()

# setting window
running = True
while running:
    
    # setting background color
    screen.fill((222, 220, 225))

    # drawing a circle
    #pygame.draw.circle(screen, (95, 56, 30), (300, 150), 25)
    screen.blit(character, (character_x, character_y))

    # moving the circle
    keys = pygame.key.get_pressed()

    # arrows
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= character_speed

    if keys[pygame.K_RIGHT] and character_x < screen_length - 100:
        character_x += character_speed

    if keys[pygame.K_UP] and character_y > 0:
        character_y -= character_speed

    if keys[pygame.K_DOWN] and character_y < screen_width -100:
        character_y += character_speed

    # letters
    if keys[pygame.K_a] and character_x > 0:
        character_x -= character_speed

    if keys[pygame.K_d] and character_x < screen_length - 100:
        character_x += character_speed

    if keys[pygame.K_w] and character_y > 0:
        character_y -= character_speed

    if keys[pygame.K_s] and character_y < screen_width -100:
        character_y += character_speed


    # setting FPS
    FPS.tick(30)

    pygame.display.update()
    
    # closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False 
             
pygame.quit()
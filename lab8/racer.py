import pygame

pygame.init()

screen_length = 568
screen_width = 750

screen = pygame.display.set_mode((screen_length, screen_width))
pygame.display.set_caption("racer task")

icon = pygame.image.load('lab8/images/isaac icon.png')
pygame.display.set_icon(icon)

FPS = pygame.time.Clock()

# background
background = pygame.image.load('lab8/images/isaac background.jpg')

# player
class player():
    """    the class of the player who will move across the screen"""
    def __init__(self, x, y, width, height, image_path):
        """    player's constructor"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (240, 160))
    
    def draw(self, screen):
        """    draw the player on the background"""
        screen.blit(self.image, (self.x, self.y))

    def move(self, dx, dy):
        """    move the player by dx and dy"""
        self.x += dx
        self.y += dy

isaac = player(screen_length / 2 - 120, screen_width * 2 / 3 - 80, 240, 160, 'lab8/images/isaac movement/isaac-down-stay.png')

running = True
while running:

    screen.blit(background, (0,0))

    # player's position
    isaac.draw(screen)

    # player's movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)

    FPS.tick(60)
       
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False 
             
pygame.quit()
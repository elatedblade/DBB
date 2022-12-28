import pygame
from fighter import Fighter

pygame.init()

# Game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# FPS
clock = pygame.time.Clock()
FPS = 60

# Define colors
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DBB")

# Load Background image
bg_image = pygame.image.load("assets/bg/bg1.png")

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 1, y - 1, 402, 32))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# Fighter instances
f1 = Fighter(200, 465)
f2 = Fighter(700, 465)


# Game Loop
run = True
while run:

    clock.tick(FPS)

    draw_bg()

    # Fighter health
    draw_health_bar(f1.health, 20, 20)
    draw_health_bar(f2.health, 580, 20)

    f1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, f2)
    # f2.move(SCREEN_WIDTH, dSCREEN_HEIGHT, screen, f1)

    # Draw fighters
    f1.draw(screen)
    f2.draw(screen)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Update display
    pygame.display.update()
    

# Exit pygame
pygame.quit()
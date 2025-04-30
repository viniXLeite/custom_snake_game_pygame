import pygame
from settings import var

# pygame setup
pygame.init()
screen = pygame.display.set_mode((var["screen_width"], var["screen_height"]))
clock = pygame.time.Clock()
running = True
dt = 0

snake_pos = pygame.Vector2(var["screen_width"]/2, var["screen_height"]/2)

while running:
    # If the user clicks the X button to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Defines screen background
    screen.fill("green")
    
    pygame.draw.circle(screen, "red", snake_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        snake_pos.y += 300 * dt
    if keys[pygame.K_a]:
        snake_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        snake_pos.x += 300 * dt

    # updates the content of the entire display
    pygame.display.flip()        

    dt = clock.tick(var["FPS"]) / 1000

pygame.quit()


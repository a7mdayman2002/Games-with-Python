import pygame

from grid import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
run = True
x_pos = 0

while run:
    clock.tick(fps)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_ESCAPE:
                run = False
            if key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12

    screen.blit(bg1, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement

    x_pos -= 1
    screen.blit(base, (x_pos, 700))
    screen.blit(base, (x_pos + 500, 700))
    screen.blit(bird_mid,bird_rect)


    if x_pos <= -500:
        x_pos = 0

    pygame.display.update()







pygame.quit()
import pygame
from os.path import join
from random import randint

#general settings
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tadijas game')
running = True

#plain surface
surf = pygame.Surface((100,100))
surf.fill('darkorange')
x = 100

#importing an image
player_surf = pygame.image.load(join('space shooter', 'images', 'player.png')).convert_alpha()
star_surf = pygame.image.load(join('space shooter', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw in game
    display_surface.fill('black')

    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    x += 0.3
    display_surface.blit(player_surf, (x, 150))
    pygame.display.update()

pygame.quit()
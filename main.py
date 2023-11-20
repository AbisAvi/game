import pygame
import config
import utils
from Sprites.Sprites import Player, Mob
from Sprites.MapSprite import Ground
import random

# git config --global user.email "daniilvolodin4@gmail.com"
# git config --global user.name AbisAvi

pygame.init()
pygame.font.init()

background = pygame.image.load("assets/zadnic.png")
background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode(
    (config.WIDTH, config.HEIGHT)
)

player = pygame.sprite.Group()
player.add(Player())

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    # screen.fill(config.COLORS["Red"])
    screen.blit(background, (0, 0))
    player.draw(screen)
    pygame.display.flip()

pygame.quit()

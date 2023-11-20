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
mobs = pygame.sprite.Group()

player_entity = Player()
player.add(player_entity)

running = True

def add_mobs():
    y1 = 200
    y2 = 150 + y1

    mobs.add(Mob(y1))
    mobs.add(Mob(y2))

add_mobs()

while running:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    mobs.update()

    if player_entity.health == 0:
        running = False

    x = mobs.sprites()[0].rect.x
    if x != config.WIDTH and len(mobs) == 2 and x < 250:
        add_mobs()


    hits = pygame.sprite.groupcollide(player, mobs, False, True)
    if hits:
        player_entity.health -= 1

    screen.fill((0, 0, 0))
    player.draw(screen)
    mobs.draw(screen)
    text = font.render(f"Hp:{player_entity.health}", False, (255, 255, 255))
    screen.blit(text, (0, 0))
    pygame.display.flip()

pygame.quit()

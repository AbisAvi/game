import pygame
import config
from Sprites.Sprites import Player, Mob
from Sprites.MapSprite import Ground
import random

# git config --global user.email "daniilvolodin4@gmail.com"
# git config --global user.name AbisAvi

pygame.init()
pygame.font.init()

background = pygame.image.load("assets/zadnic.png")
background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))

font = pygame.font.SysFont(pygame.font.get_default_font(), 40)

screen = pygame.display.set_mode(
    (config.WIDTH, config.HEIGHT)
)

player = pygame.sprite.Group()
player.add(Player())
mobs = pygame.sprite.Group()
clock = pygame.time.Clock()

player_entity = Player()
player.add(player_entity)

running = True
score = 0


def add_mobs():
    y1 = random.randint(10, config.HEIGHT - 10)
    mobs.add(Mob(y1))


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
    if x != config.WIDTH and len(mobs) == 1 and x < 125:
        add_mobs()
    hits = pygame.sprite.groupcollide(player, mobs, False, True)
    if hits:
        player_entity.health -= 1

    hits = pygame.sprite.groupcollide(player_entity.bullets, mobs, True, False)
    if hits:
        keys = list(hits.keys())
        mob = hits.get(keys[0], 0)
        if mob == 0:
            pass
        else:
            mob[0].kill()
            Mob.mobs_killed += 1
            add_mobs()
            score += 1

    screen.fill((0, 0, 0))
    player.draw(screen)
    mobs.draw(screen)
    player_entity.bullets.draw(screen)
    bound_rendered = font.render(f"Score: {score}", True, (0, 255, 255))
    screen.blit(bound_rendered, (0, 0))
    pygame.display.flip()

pygame.quit()

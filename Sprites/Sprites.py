import pygame.key
from pygame.sprite import Sprite
from pygame import Surface, image, transform, rect
import config
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("assets/fb.png")
        self.rect = self.image.get_rect()

        self.bullets = pygame.sprite.Group()

        self.money = 0
        self.speed_x = 0
        self.speed_y = 0
        self.health = 1
        self.points = 0
        self.resist = 5

        self.ticks = 0
        self.fire_tick = 0

    def update(self, *args, **kwargs):
        self.ticks += 1
        self.bullets.update()
        x, y = self.rect.topleft
        width, height = self.rect.size

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:  # -x
            self.speed_x -= 7
        elif keys[pygame.K_d]:  # x
            self.speed_x += 7
        elif keys[pygame.K_w]:  # y
            self.speed_y -= 7
        elif keys[pygame.K_s]:
            self.speed_y += 7
        elif keys[pygame.K_r] and self.ticks - self.fire_tick > config.FRAMERATE * 1:
            bullet = Bullet(self)
            self.bullets.add(bullet)
            self.fire_tick = self.ticks

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        self.speed_x = 0
        self.speed_y = 0

        if x < 0:
            self.rect.x = 0
        if x > config.WIDTH - width:
            self.rect.x = config.WIDTH - width
        if y < 0:
            self.rect.y = 0
        if y > config.HEIGHT - height:
            self.rect.y = config.HEIGHT - height


class Bullet(Sprite):
    def __init__(self, player: Player):
        Sprite.__init__(self)
        self.images = [
            image.load("assets/mysor.png")
        ]
        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.speed_x = 5

        self.rect.center = player.rect.center

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x > config.WIDTH - self.rect.width:
            self.kill()


class Mob(Sprite):
    mob_speed = -10
    mobs_killed = 0

    def __init__(self, y):
        Sprite.__init__(self)
        self.images = [
            image.load("assets/mysor.png")
        ]
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()
        self.speed_x = Mob.mob_speed

        self.rect.center = (
            config.WIDTH - 32,
            y
        )

    def update(self):
        self.speed_x = Mob.mob_speed + Mob.mobs_killed // -5

        self.rect.x += self.speed_x
        if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
            self.kill()

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y

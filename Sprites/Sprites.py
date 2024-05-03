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

        self.money = 0
        self.speed_x = 0
        self.speed_y = 0
        self.health = 10
        self.points = 0
        self.resist = 5


    def update(self, *args, **kwargs):
        x, y = self.rect.topleft
        width, height = self.rect.size

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # -x
            self.speed_x -= 6
        elif keys[pygame.K_d]:  # x
            self.speed_x += 6
        elif keys[pygame.K_w]:  # y
            self.speed_y -= 6
        elif keys[pygame.K_s]:
            self.speed_y += 6

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


class Player1(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.index = 0

        self.images = [
            image.load("assets/fb.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (64, 32)),
            self.images
        ))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)

        self.health = 10
        self.points = 0
        self.resist = 5

        self.speed_y = 3
        self.cooldown = 13

    def update(self):
        self.speed_y += 1
        self.update_image_move(0)
        if self.cooldown < 13:
            self.cooldown += 1

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.cooldown == 13:
            self.speed_y = -10
            self.cooldown = 0
        if key[pygame.K_LSHIFT]:
            self.speed_y = 1
            self.rect.height = 32
        else:
            self.rect.height = 32

        self.rect.y += self.speed_y
        if self.rect.y > config.HEIGHT - self.rect.height or self.rect.y < 0:
            self.rect.y -= self.speed_y
            # self.speed_y *= 0.95

    def update_image(self, index):
        if self.index != index:
            self.index = index
            self.image = self.images[self.index]

    def update_image_move(self, move: int):
        image = self.images[self.index]
        if move < 0:
            image = transform.flip(image, 1, 0)
        self.image = image

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y

    def get_knockback(self):
        self.rect.y += -self.speed_y


class Mob(Sprite):
    def __init__(self, y):
        Sprite.__init__(self)
        self.images = [
            image.load("assets/mysor.png")
        ]
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()
        self.speed_x = -6

        self.rect.center = (
            config.WIDTH - 32,
            y
        )

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
            self.kill()

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y

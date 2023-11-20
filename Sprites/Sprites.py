import pygame.key
from pygame.sprite import Sprite
from pygame import Surface, image, transform, rect
import config
import random
import utils


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.index = 0

        self.images = [
            image.load("assets/spman.png"),
            image.load("assets/spman.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (64, 32)),
            self.images
        ))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)

        self.health = 1
        self.points = 0
        self.resist = 5

        self.speed_y = 3

    def update(self):
        self.speed_y += 1
        self.update_image_move(0)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.speed_y = -5
        if key[pygame.K_LSHIFT]:
            self.speed_y = 1
            self.rect.height = 16
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
        angle = 45 * move
        # image = transform.rotate(self.images[self.index], angle)
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
        self.image =  image.load("assets/bochka.png")
        self.rect = self.image.get_rect()
        self.rect.center = (
            config.WIDTH - 32,
            y
        )

        self.speed_x = -3

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
            self.kill()

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y

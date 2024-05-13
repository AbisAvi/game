from pygame import image
from pygame.sprite import Sprite

import Sprites
import config


class Mob(Sprite):
    def __init__(self, player: Sprites.Player):
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

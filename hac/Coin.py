import pygame
import math

size = (800, 600)
screen = pygame.display.set_mode(size)

def normalize_vector(vector):
    if vector == [0, 0]:
        return [0, 0]
    pythagoras = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
    return (vector[0] / pythagoras, vector[1] / pythagoras)


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface([8, 8])
        self.image.fill(pygame.Color('gold'))
        self.rect = self.image.get_rect(x=pos[0], y=pos[1])
        self.radius = self.rect.width / 2
        self.pos = list(pos)


    def render(self, surface):
        surface.blit(self.image, self.pos)

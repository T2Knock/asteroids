import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

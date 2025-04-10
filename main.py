import pygame

from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = Asteroid()

    updatables.add(player)
    drawables.add(player)
    updatables.add(asteroid)
    drawables.add(asteroid)
    asteroids.add(asteroid)

    print(updatables, drawables)

    dt = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatables.update(dt)
        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000  # limit the framerate to 60 FPS

    pygame.quit()


if __name__ == "__main__":
    main()

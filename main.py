import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfeild import AsteroidField

def main():
    # Initialize Pygame, screen and clock
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Create sprite groups and set up containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    #initialize player in middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Game loop
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

#call main function
if __name__ == "__main__":
    main()

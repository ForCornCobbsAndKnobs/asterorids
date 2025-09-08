import pygame, constants, circleshape, player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    pb = player.PLAYER(x = constants.SCREEN_WIDTH/2, y = constants.SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pb.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()

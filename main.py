import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        AsteroidField.containers = (updatable)
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        Shot.containers = (shots, updatable, drawable)
        pygame.init
        print("Starting asteroids!", f"Screen width: {SCREEN_WIDTH}", f"Screen height: {SCREEN_HEIGHT}")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        field = AsteroidField()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        while True:
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
              screen.fill((0,0,0))
              for x in drawable:
                   x.draw(screen)
              for x in updatable:
                   x.update(dt)
              for x in asteroids:
                   if x.collision(player):
                    print('Game Over!')
                    pygame.display.quit
                    pygame.quit()
              for y in shots:
                    for x in asteroids:
                         if x.collision(y):
                              x.split()
                              y.kill()
              pygame.display.flip()
              dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
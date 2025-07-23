import pygame
import constants
from shot import Shot
from asteroids import Asteroid
from constants import *
from asteroidfield import AsteroidField
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f'''
        Screen width: {constants.SCREEN_WIDTH} 
        Screen height: {constants.SCREEN_HEIGHT}''')
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    #game timer
    clock = pygame.time.Clock()
    dt = 0

    #create groupings
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    #create containers
    Shot.containers = (shots,updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    # Initialize player
    player= Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    #Game loop
    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       updatable.update(dt)
       for object in updatable:
           if isinstance(object, Asteroid):
               if object.collision(player) == True:
                   print('Game over!')
                   exit()
       screen.fill("black")
       for sprite in drawable:
           sprite.draw(screen)
       pygame.display.flip()
       clock.tick(60)
       dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()

import pygame
import constants
from constants import *
from player import Player

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

    # Initialize player
    player= Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    #Game loop
    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       screen.fill("black")
       player.draw(screen)
       pygame.display.flip()
       clock.tick(60)
       dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()

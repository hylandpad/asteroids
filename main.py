import pygame
import constants
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f'''
        Screen width: {constants.SCREEN_WIDTH} 
        Screen height: {constants.SCREEN_HEIGHT}''')
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    #Game loop
    while True:
       for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       screen.fill("black")
       pygame.display.flip() 

if __name__ == "__main__":
    main()

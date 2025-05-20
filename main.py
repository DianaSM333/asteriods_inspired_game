import pygame
# importing all the constants
from constants import *
def main():
    pygame.init()   # initializing the game
    print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    '''
    Video games are generally built using a game loop, the simplest loop has 3 steps
    1.) Check for payer inputs
    2.) Update the game world
    3.) Draw the game to the screen - needs to happen many times per second
    '''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip() #update the contents of the entire display



# this lines ensures that the main function is only called when the program runs directly; wont run if imported as a module

if __name__ == "__main__":
    main()
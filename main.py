import sys

import pygame

from asteroid import Asteroid
# importing all the constants
from constants import *
from player import Player
from asteroidfield import AsteroidField
from bullet import Shot

def main():
    pygame.init()   # initializing the game
    c = pygame.time.Clock()
    dt = 0          # delta is used to represent the amount of time that has passed since the last frame was drawn
    print("Starting Asteroids!")


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)    # player has to be added after the group is created

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)  # this ensures that every instance of the Asteroid class is automatically added to these groups upon creation

    AsteroidField.containers = (updatable)
    field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
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

        updatable.update(dt)    # updates position before it is rendered

        #checks for collision between player and asteroids
        for a in asteroids:
            if a.collision_check(player):
                sys.exit("Game Over")
        screen.fill((0, 0, 0))

        # draws all the sprites
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip() #update the contents of the entire display
        dt = c.tick(60) # pauses game loop until 1/60th of a second has passed also returns the amount of time that has passed since it was last called or delta
        dt /= 1000 # converting from miliselsconds to seconds





# this lines ensures that the main function is only called when the program runs directly; wont run if imported as a module

if __name__ == "__main__":
    main()
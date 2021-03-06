import globals
import pygame
from inputs import Inputs
from entity import Entity
from render import render
from display import update_display_mode, toggle_fullscreen
from update import update
from player import Player
from block import Block
from collision import checkCollision

globals.width = 640
globals.height = 480
globals.fullscreen = False

def main():

	pygame.init()
	globals.pygame = pygame # assign global pygame for other modules to reference
	globals.inputs = Inputs(pygame) # assign global inputs for other modules to reference
	update_display_mode() # now that the global display properties have been set up, update the display
	clock = pygame.time.Clock() # clock to tick / manage delta

	globals.entities = [] # contains every object that will be drawn in the game

	globals.entities.append(Player(100, 100)) # create a new Player entity at (100, 100)

	loop = True # for controlling the game loop

	globals.window.fill((255, 255, 255))

	while(loop):
		clock.tick(60) # tick the clock with a target 60 fps
		globals.window.fill((255, 255, 255))

		globals.inputs.update() # refresh inputs


		update() # update all globals.entities
		checkCollision() # check collision on globals.entities
		render() # draw all globals.entities

		if(globals.inputs.isKeyDown("enter")): toggle_fullscreen() # space bar toggles fullscreen
		if(globals.inputs.isKeyDown("escape")): loop = False # escape key exits game
		if(globals.inputs.isQuitPressed()): loop = False # red 'x' button exits game

		pygame.display.flip() # flip the display, which finally shows our render

	pygame.quit() # unload pygame modules

main() # initiate game
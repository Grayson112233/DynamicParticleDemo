import globals
import pygame

class Entity(): # the base for all objects that will be drawn on the screen in the game

	def __init__(self):
		self.x = 0 # default x coord
		self.y = 0 # default y coord
		self.collides = False

	def update(self): # move the entity with the arrow keys
		if(globals.inputs.isKeyDown("up")):
			self.y -= 5
		if(globals.inputs.isKeyDown("down")):
			self.y += 5
		if(globals.inputs.isKeyDown("right")):
			self.x += 5
		if(globals.inputs.isKeyDown("left")):
			self.x -= 5

	def getType(self):
		return "Entity"

	def clamp(self, image):
		if self.x < 0: self.x = 0
		if self.y < 0: self.y = 0
		if self.x > globals.window.get_width() - image.get_width(): self.x = globals.window.get_width() - image.get_width()
		if self.y > globals.window.get_height() - image.get_height(): self.y = globals.window.get_height() - image.get_height()
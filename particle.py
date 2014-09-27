import pygame
import globals
import random

class Particle():

	def __init__(self, x, y, lifespan=50, size=None):
		if(size == None): size = random.randrange(4, 8, 1)
		self.collides = False
		self.x = x
		self.y = y
		self.x_v = random.randrange(-10, 10, 1) / 10
		self.y_v = random.randrange(-10, 10, 1) / 10
		self.width = size
		self.height = size
		self.age = lifespan

	def update(self):
		self.x += self.x_v
		self.y += self.y_v
		self.age -= 1
		if(self.age <= 0): self.kill()

	def draw(self):
		pygame.draw.rect(globals.window, (0,0,0), (self.x, self.y, self.width, self.height), 0)

	def kill(self):
		globals.entities.remove(self)

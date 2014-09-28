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

		self.surface = pygame.Surface((self.width, self.height))
		self.surface.fill((0,0,0))
		self.surface.set_alpha(255)
		self.alpha_mod = (254 / lifespan)

	def update(self):
		self.x += self.x_v
		self.y += self.y_v
		self.age -= 1
		if(self.age <= 0): self.kill()
		self.surface.set_alpha(self.surface.get_alpha() - self.alpha_mod)

	def draw(self):
		globals.window.blit(self.surface, (self.x, self.y))

	def kill(self):
		globals.entities.remove(self)

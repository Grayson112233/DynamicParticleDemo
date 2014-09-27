import globals
import pygame
from hitbox import Hitbox

from entity import Entity

class Block(Entity):


	def __init__(self, x, y):

		Entity.__init__(self)

		self.x = x
		self.y = y
		self.collides = True

		self.img = pygame.image.load("res/pics/box.png")

		self.hitbox = Hitbox(self.x, self.y, self.img.get_width(), self.img.get_height())

	def update(self):
		self.hitbox.update(self.x, self.y)

	def draw(self):
		globals.window.blit(self.img, (self.x, self.y))

	def getType(self):
		return "Block"

	def collide(self, entity):
		pass
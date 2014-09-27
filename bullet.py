import pygame
import globals
from hitbox import Hitbox

class Bullet():

	def __init__(self, x, y, direction, speed=10):
		self.collides = True
		self.x = x
		self.y = y
		self.x_v = 0
		self.y_v = 0
		self.img = pygame.image.load("res/pics/bullet.png")
		self.hitbox = Hitbox(self.x, self.y, self.img.get_width(), self.img.get_height())
		if(direction == "up"):
			self.y_v = -speed
		elif(direction == "down"):
			self.y_v = speed
		elif(direction == "right"):
			self.x_v = speed
		elif(direction == "left"):
			self.x_v = -speed

	def update(self):
		self.x += self.x_v
		self.y += self.y_v
		self.hitbox.update(self.x, self.y)
		if(self.x < 0): self.kill()
		if(self.y < 0): self.kill()
		if(self.x > globals.width): self.kill()
		if(self.y > globals.height): self.kill()

	def draw(self):
		globals.window.blit(self.img, (self.x, self.y))

	def collide(self, entity):
		pass

	def kill(self):
		globals.entities.remove(self)

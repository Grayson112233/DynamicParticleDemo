import globals
import pygame
from entity import Entity
from hitbox import Hitbox
from bullet import Bullet
from particle import Particle
import random

class Player(Entity):

	def __init__(self, x, y):
		Entity.__init__(self)
		self.x = x
		self.y = y
		self.oldx = x
		self.oldy = y
		self.collides = True

		self.img_body = pygame.image.load("res/pics/body.png")

		self.hitbox = Hitbox(self.x, self.y, self.img_body.get_width(), self.img_body.get_height())

		self.up = 0
		self.down = 0
		self.left = 0
		self.right = 0
		self.max_direction_accel = 5
		self.direction_accel = 0.2

		self.cooldown = 30
		self.cooldown_timer = 0

		self.is_clamp = True

	def update(self):
		self.oldx = self.x
		self.oldy = self.y

		if(globals.inputs.k_k_down):
			self.is_clamp = not self.is_clamp

		if(globals.inputs.isKeyDown("w")):
			self.up += self.direction_accel
		else:
			self.up -= self.direction_accel
		if(globals.inputs.isKeyDown("a")):
			self.left += self.direction_accel
		else:
			self.left -= self.direction_accel
		if(globals.inputs.isKeyDown("s")):
			self.down += self.direction_accel
		else:
			self.down -= self.direction_accel
		if(globals.inputs.isKeyDown("d")):
			self.right += self.direction_accel
		else:
			self.right -= self.direction_accel

		if(self.up > self.max_direction_accel): self.up = self.max_direction_accel
		if(self.down > self.max_direction_accel): self.down = self.max_direction_accel
		if(self.left > self.max_direction_accel): self.left = self.max_direction_accel
		if(self.right > self.max_direction_accel): self.right = self.max_direction_accel

		if(self.up < 0): self.up = 0
		if(self.down < 0): self.down = 0
		if(self.left < 0): self.left = 0
		if(self.right < 0): self.right = 0

		total_speed = self.up + self.down + self.right + self.left
		if(total_speed > 0):
			globals.entities.append(Particle(self.x + (self.img_body.get_width() / 2), self.y + (self.img_body.get_height() / 2)))
		
		self.y -= self.up
		self.y += self.down
		self.x -= self.left
		self.x += self.right

		if(self.is_clamp): self.clamp(self.img_body)

		self.hitbox.update(self.x, self.y)

		if(self.cooldown_timer > 0): 
			self.cooldown_timer -= 1
		else:
			if(globals.inputs.isKeyDown("right")):
				globals.entities.append(Bullet(self.x, self.y, "right"))
			elif(globals.inputs.isKeyDown("left")):
				globals.entities.append(Bullet(self.x, self.y, "left"))
			elif(globals.inputs.isKeyDown("up")):
				globals.entities.append(Bullet(self.x, self.y, "up"))
			elif(globals.inputs.isKeyDown("down")):
				globals.entities.append(Bullet(self.x, self.y, "down"))
			self.cooldown_timer = self.cooldown

	def draw(self):
		globals.window.blit(self.img_body, (self.x, self.y))

	def getType(self):
		return "Player"

	def collide(self, entity):
		pass

	def getCenter(self):
		x = (self.x - self.hitbox.width) / 2
		y = (self.y - self.hitbox.height) / 2
		return (x, y)
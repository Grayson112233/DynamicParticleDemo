class Hitbox():

	def __init__(self, x, y, width, height):

		self.top = 0
		self.left = 0
		self.width = 0
		self.height = 0

		self.setup(x, y, width, height)

	def getCorners(self):
		return [(self.left, self.top), (self.left + self.width, self.top), (self.left, self.top + self.height), (self.left + self.width, self.top+ self.height)]

	def setup(self, top, left, width, height):
		self.width = width
		self.height = height
		self.top = top
		self.left = left

	def update(self, x, y):
		self.left = x
		self.top = y

	def collide_hitbox(self, hitbox):
		corners = hitbox.getCorners()
		for corner in corners:
			if(self.collide_point(corner[0], corner[1])):
				return True
		return False

	def collide_point(self, x, y):
		if(x >= self.left and x <= self.left + self.width):
			if(y >= self.top and y <= self.top + self.height):
				return True
		return False
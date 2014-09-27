import globals

def render():
	for entity in globals.entities:
		entity.draw()
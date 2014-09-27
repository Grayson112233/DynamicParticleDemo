# update all entities
import globals

def update():
	for entity in globals.entities:
		entity.update()
import globals

def checkCollision():
	for i in range(len(globals.entities)):
		if(globals.entities[i].collides):
			for j in range(len(globals.entities)):
				if(i != j and globals.entities[j].collides):
					if(globals.entities[j].hitbox.collide_hitbox(globals.entities[i].hitbox) or globals.entities[i].hitbox.collide_hitbox(globals.entities[j].hitbox)):
						globals.entities[i].collide(globals.entities[j])
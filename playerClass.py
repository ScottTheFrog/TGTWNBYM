import pygame
import math

screen = pygame.display.set_mode([800,600])
rects = {}
class colission():
	def __init__(self,x,y,w,h,color,solid,realname):
		self.x = x
		self.y = y
		self.w = w 
		self.h = h
		self.color = color
		self.name = 0
		self.solid = solid
		self.realname = realname

	def create(self):
		self.name = pygame.Rect(self.x,self.y,self.w,self.h)
		if not self.realname in rects:
			rects[self.realname]=[self.name,self.solid]
		rectobj = rects.get(self.realname)[0]
		if self.name != rectobj:
			self.name = rectobj
		pygame.draw.rect(screen,self.color,rectobj)

class playerObject:
	def __init__(self,location,speed,friction,time):
		self.location = [0.0,0.0]
		self.speed = speed
		self.velocity = [0.0,0.0]
		self.friction = friction
		self.directionVector = [0,0]
		self.collisionRect = pygame.Rect(0,0,0,0)
		self.time = time

	def playerInputCheck(self):
		##GET KEYPRESS INPUT FROM KEYBOARD AND CHANGE VECTOR VALUE
		keypress = pygame.key.get_pressed()
		if keypress[pygame.K_LEFT]:
			self.directionVector[0] = -1
		elif keypress[pygame.K_RIGHT]:
			self.directionVector[0] = 1
		else:
			self.directionVector[0] = 0

		if keypress[pygame.K_UP]:
			self.directionVector[1] = -1
		elif keypress[pygame.K_DOWN]:
			self.directionVector[1] = 1
		else:
			self.directionVector[1] = 0


	def playerMove(self,time):
		self.time = time
		##MAKE collisionRect
		self.collisionRect = pygame.Rect(self.location[0],self.location[1],64,64)

		##ADD VELOCITY TO THE LOCATION
		self.location[0] += self.velocity[0]
		self.location[1] += self.velocity[1]

		##MULTIPLY THE DIRECTION BY THE SPEED
		self.velocity[0] = self.directionVector[0] * self.speed * ( 1.0 /(self.time +1))
		self.velocity[1] = self.directionVector[1] * self.speed * ( 1.0 /(self.time+1))

	def playerColission(self):
		for rect in rects:
			rectlist = rects.get(rect)
			rectcoordinates = rectlist[0] 

			def act(a,b):
				print(a)
				print(b)
				if b == 0:
					self.location[a] -= self.velocity[a] -( rectcoordinates[a] + (self.location[a] -64))
					if rectlist[1]:
						rectcoordinates[a] -= self.velocity[a]  *-0.5

				else:
					self.location[a] -= self.velocity[a] -( (rectcoordinates[a] - rectcoordinates[a+2]) - self.location[a]) 
					if rectlist[1]:
						rectcoordinates[a] += self.velocity[a] *0.5

			if self.collisionRect.colliderect(rectcoordinates):

				##X
				if self.location[0] + 64 >= rectcoordinates[0] and self.location[0] + 64 <= rectcoordinates[0]+13:
					act(0,1)

				elif self.location[0] <= (rectcoordinates[0] + rectcoordinates[2]) and self.location[0] >= (rectcoordinates[0] + rectcoordinates[2])-13:
					act(0,0)
				##Y
				if self.location[1] + 64 >= rectcoordinates[1] and self.location[1] + 64 <= rectcoordinates[1]+13:
					act(1,1)

				elif self.location[1] <= (rectcoordinates[1] + rectcoordinates[3]) and self.location[1] >= (rectcoordinates[1] + rectcoordinates[3]) -13:
					act(1,0)
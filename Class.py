import pygame
import math

screen = pygame.display.set_mode([800,600])
allrects = {}

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
		if not self.realname in allrects:
			allrects[self.realname]=[self.name,self.solid]
		rectobj = allrects.get(self.realname)[0]
		if self.name != rectobj:
			self.name = rectobj
		pygame.draw.rect(screen,self.color,rectobj)

class playerobj:
	def __init__(self,x,y,s,ts,a,name,mov):
		self.x = x
		self.y = y
		self.s = s
		self.sy = s
		self.sx = s
		self.ts = ts
		self.a = a 
		self.name = name
		self.mov = mov
		self.movx = False
		self.movy = False
		self.directiony = 0
		self.directionx = 0

	def mcheck(self):
		self.name = pygame.Rect(self.x,self.y,64,64)
		k = pygame.key.get_pressed()
		if k[pygame.K_LEFT] or k[pygame.K_RIGHT]:
			self.movx = True
			if self.sx ==0:
				self.sx = 1
		if k[pygame.K_UP] or k[pygame.K_DOWN]:
			self.movy = True
			if self.sy ==0:
				self.sy = 1
				
		if not k[pygame.K_UP] and not k[pygame.K_DOWN] :
			self.movy = False
		if not k[pygame.K_LEFT] and not k[pygame.K_RIGHT]:	
			self.movx = False

		if k[pygame.K_UP]:
			self.directiony = 1
		elif k[pygame.K_DOWN]:
			self.directiony = 2

		if k[pygame.K_RIGHT]:
			self.directionx = 1
		elif k[pygame.K_LEFT]:
			self.directionx = 2


		if self.directiony ==1:
			self.y -=self.sy
		elif self.directiony ==2:
			self.y +=self.sy

		if self.directionx ==1:
			self.x +=self.sx
		elif self.directionx ==2:
			self.x -=self.sx


		if self.movx and self.directionx != 0:
			self.sx *= self.a
			if self.sx >=self.ts:
				self.sx = self.ts
		else:
			self.sx -=1
			if self.sx < 0.5:
				self.sx = 0
				self.directionx = 0
				self.x = round(self.x)

		if self.movy and self.directiony != 0:
			self.sy *= self.a
			if self.sy >=self.ts:
				self.sy = self.ts
		else:
			self.sy -= 1
			if self.sy < 0.5:
				self.sy = 0
				self.directiony = 0
				self.y = round(self.y)

	def colission(self):
		xw = self.x + 64;
		yw = self.y + 64;
		for i in allrects :
			b = allrects.get(i)
			if self.name.colliderect(b[0]):
				self.sx = round(self.sx)
				self.sy = round(self.sy)
				
				if xw >= b[0][0] and xw <= b[0][0]+13:
					if b[1]:
						b[0][0] += self.sx/2
						self.x -= self.sx
					else:
						self.x -= self.sx

				elif self.x <= (b[0][0] + b[0][2]) and self.x >= (b[0][0] + b[0][2])-13:
					if b[1]:
						b[0][0] -= self.sx/2
						self.x += self.sx
					else:
						self.x += self.sx

				if yw >= b[0][1] and yw <= b[0][1]+13:
					if b[1]:
						b[0][1] += self.sy/2
						self.y -= self.sy
					else:
						self.y -= self.sy

				elif self.y <= (b[0][1] + b[0][3]) and self.y >= (b[0][1] + b[0][3]) -13:
					if b[1]:
						b[0][1] -= self.sy/2
						self.y += self.sy
					else:
						self.y += self.sy
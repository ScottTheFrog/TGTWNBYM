import pygame
screen = pygame.display.set_mode([800,600])
class colission():
	def __init__(self,x,y,w,h,color,movable,rects,time):
		self.x = x
		self.y = y
		self.w = w 
		self.h = h
		self.color = color
		self.movable = movable
		self.colliderName = time
		rects[self.colliderName]=[[self.x,self.y,self.w,self.h],self.movable,self.color,time]
	def create(self,rects):
		rectobj = rects.get(self.colliderName)[0]
		color = rects.get(self.colliderName)[2]
		pygame.draw.rect(screen,color,rectobj)
		print(rectobj)

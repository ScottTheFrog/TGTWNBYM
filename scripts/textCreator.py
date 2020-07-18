import pygame
screen = pygame.display.set_mode([800,600])
class Text():
	def __init__(self,x,y,text,textScale,color):
		self.pos = [x,y]
		self.text = text
		self.textScale = textScale
		self.textFont = pygame.font.Font("freesansbold.ttf",self.textScale)

		self.color = color
	def render(self,text):
		self.text = text
		self.textRender = self.textFont.render(str(text),0,self.color)
		screen.blit(self.textRender,self.pos)

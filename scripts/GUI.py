import pygame
screen = pygame.display.set_mode([800,600])
class gameUI():
	def __init__(self):
		self.mousePos = []
		self.mouseClick =  []
		self.mouseRect = []

		self.playMapButtonRect = pygame.Rect(64,64,256,64)
		self.playMapButtonColor = [55,110,55]

		self.createMapButtonRect = pygame.Rect(64,144,256,64)
		self.createMapButtonColor = [110,22,22]

		self.goToThis = 0
		self.run = True
	def drawUI(self):
		pygame.draw.rect(screen,self.playMapButtonColor,self.playMapButtonRect)
		pygame.draw.rect(screen,self.createMapButtonColor,self.createMapButtonRect)
		pygame.draw.rect(screen,[255,0,0],self.mouseRect)

	def getInput(self):
		self.mousePos = [pygame.mouse.get_pos()[0]-8,pygame.mouse.get_pos()[1]-8]
		self.mouseClick =  [pygame.mouse.get_pressed()[0],pygame.mouse.get_pressed()[2]]

		self.mouseRect  = pygame.Rect(self.mousePos,[16,16])

	def inputCheck(self):
		if self.mouseRect.colliderect(self.playMapButtonRect):
			self.goToThis = self.mouseClick[0] 
		elif self.mouseRect.colliderect(self.createMapButtonRect):
			self.goToThis = self.mouseClick[0] * 2



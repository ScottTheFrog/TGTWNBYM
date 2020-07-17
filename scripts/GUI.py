import pygame
screen = pygame.display.set_mode([800,600])
class gameUI():
	def __init__(self):
		self.mousePos = []
		self.mouseClick =  []
		self.mouseRect = []

		self.playMapButtonRect = pygame.Rect(64,64,256,64)
		self.playMapButtonColor = [55,110,55]

		self.goToThis = 0
		self.run = True
	def drawUI(self):
		pygame.draw.rect(screen,self.playMapButtonColor,self.playMapButtonRect)
		pygame.draw.rect(screen,[255,0,0],self.mouseRect)

	def getInput(self):
		self.mousePos = [pygame.mouse.get_pos()[0]-8,pygame.mouse.get_pos()[1]-8]
		self.mouseClick =  [pygame.mouse.get_pressed()[0],pygame.mouse.get_pressed()[2]]

		self.mouseRect  = pygame.Rect(self.mousePos,[16,16])

	def inputCheck(self):
		self.goToThis = int(self.mouseRect.colliderect(self.playMapButtonRect)) * self.mouseClick[0] 



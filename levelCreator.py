import pygame
import rectClass
screen = pygame.display.set_mode([800,600])
pygame.init()
run = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,600])
rects = {}
rectList = [rectClass.colission(200,100,200,50,[170,170,170],True,rects),
			rectClass.colission(0,125,50,100,[170,170,170],False,rects),
			rectClass.colission(0,500,800,100,[170,0,0],False,rects)

			]

class AAAAAAAAAAAAAAAAA():
	def __init__(self):
		self.startPos = [300,300]
		self.endPos = [300,300]
		self.widthheight = [50,50]
		self.createdCollider = False
		self.color = [0,0,0]
	def createCollider(self):
		self.mousePos = pygame.mouse.get_pos()
		self.mouseClick =  pygame.mouse.get_pressed()[0]		
		self.endPos[0] = self.mousePos[0] 
		self.endPos[1] = self.mousePos[1]
		self.widthheight = [(self.endPos[0] - self.startPos[0]),(self.endPos[1] - self.startPos[1])]
		self.collisionRect = pygame.Rect(self.startPos,self.widthheight)
		if self.mouseClick == 1:
			self.createdCollider = True
			pygame.draw.rect(screen,[255,0,0],self.collisionRect)
		else:
			if self.createdCollider:
				print(self.widthheight)
				try:
					self.color = "a"#input("COLOR : ")
					self.color = self.color.split(" ")
					self.color = [int(self.color[0]),int(self.color[1]),int(self.color[2])]
				except:
					print("ERROR WHILE TRYING TO DECODE COLOR")
					self.color = [self.endPos[0]/5,self.startPos[1]/5,self.startPos[0]/5]
				rectList.append(rectClass.colission(self.collisionRect[0],self.collisionRect[1],
													self.collisionRect[2],self.collisionRect[3],
													self.color,False,rects))
				self.createdCollider = False
			self.startPos[0] = self.mousePos[0] 
			self.startPos[1] = self.mousePos[1] 

def createColliders():
	for name in range(0,len(rectList)):
		rectList[name].create(rects)

AAAAAAA = AAAAAAAAAAAAAAAAA()
while run:
	clock.tick()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((255,255,255))
	AAAAAAA.createCollider()
	createColliders()
	pygame.display.update()
pygame.quit()
import pygame
screen = pygame.display.set_mode([800,600])

class CreateRECTS():
	def __init__(self):
		from createColliders import cCollider

		self.cColliderObj = cCollider()
		self.cColliderObj.createColliders()

		self.cColliderObj.FUCKINGBUGS(-32,-32,1600,32,[0,0,0],False,94857)
		self.cColliderObj.FUCKINGBUGS(800,-32,1600,1600,[0,0,0],False,780780)
		self.cColliderObj.FUCKINGBUGS(-32,600,1600,32,[0,0,0],False,467467)
		self.cColliderObj.FUCKINGBUGS(-32,-32,32,1600,[0,0,0],False,13513)

		self.startPos = [300,300]
		self.endPos = [300,300]
		self.widthheight = [50,50]
		self.createdCollider = False
		self.color = [0,0,0]
		self.gettingInput = True
		self.inputString = ""
		self.output = "maps/map4.pickle"
		self.delay = 1
		self.mouseClick = 0
		self.time = 0
	def getInput(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == 13:
					self.gettingInput = False
					print(self.output)
				else:
					self.inputString += event.unicode
					print(self.inputString)
		self.output = "maps/" + str(self.inputString)+".pickle" 



	def createCollider(self,fps):
		import math
		self.cColliderObj.renderColliders()
		self.mousePos = pygame.mouse.get_pos()
		if self.delay <= 0:
			self.mouseClick =  pygame.mouse.get_pressed()[0]
		self.endPos[0] = self.mousePos[0] 
		self.endPos[1] = self.mousePos[1]
		if self.endPos[0] % 32 != 0:
			self.endPos[0] = self.endPos[0] + (round(self.endPos[0]/32) - self.endPos[0]/32) *32

		if self.endPos[1] % 32 != 0:
			self.endPos[1] = self.endPos[1] + (round(self.endPos[1]/32) - self.endPos[1]/32) *32

		self.widthheight = [(self.endPos[0] - self.startPos[0]),(self.endPos[1] - self.startPos[1])]
		self.collisionRect = pygame.Rect(self.startPos,self.widthheight)
		if self.mouseClick == 1:
			self.time += fps
			self.createdCollider = True
			pygame.draw.rect(screen,[255,0,0],self.collisionRect)
		else:
			if self.createdCollider:
				try:
					self.color = "a"#input("COLOR : ")
					self.color = self.color.split(" ")
					self.color = [int(self.color[0]),int(self.color[1]),int(self.color[2])]
				except:
					print("ERROR WHILE TRYING TO DECODE COLOR")
					self.color = [self.endPos[0]/5,self.startPos[1]/5,self.startPos[0]/5]

				self.cColliderObj.FUCKINGBUGS(self.collisionRect[0],self.collisionRect[1],
										self.collisionRect[2],self.collisionRect[3],
										self.color,False,self.time)
				print(self.time)

				self.createdCollider = False
			self.startPos[0] = self.mousePos[0] 
			self.startPos[1] = self.mousePos[1]

			if self.startPos[0] % 32 != 0:
				self.startPos[0] = self.startPos[0] + (round(self.startPos[0]/32) - self.startPos[0]/32) *32

			if self.startPos[1] % 32 != 0:
				self.startPos[1] = self.startPos[1] + (round(self.startPos[1]/32) - self.startPos[1]/32) *32

	def dumpPickle(self):
		import pickle
		pickleOUT = open(self.output, "wb")
		pickle.dump(self.cColliderObj.rects, pickleOUT)
		pickleOUT.close()
		print("OVERWRITTEN PICKLE MAP FILE")
	def openPickle(self):
		import pickle
		print("OPENING PICKLE MAP FILE")
		pickleIN = open(self.output, "rb")
		self.cColliderObj.rects = pickle.load(pickleIN)
		pickleIN.close()
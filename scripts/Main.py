import pygame
import playerClass
import rectClass
import random
from createColliders import cCollider
from GUI import gameUI
from levelCreator import CreateRECTS
from textCreator import Text

pygame.init()
clock = pygame.time.Clock()
#area = pygame.Surface([3000,3000])
#playerimg = pygame.image.load("Sprites/creepy.png")
screen = pygame.display.set_caption("RogueLike Game")
screen = pygame.display.set_mode([800,600])

UI = gameUI()

playerInstance = playerClass.playerObject(0,200,3,1)

fps = 60
FPStext = Text(16,16,fps,30,[0,0,0])
#sound = pygame.mixer.Sound("sound.wav")
#sound.play()
#sound.set_volume(0.25)

colliderCreator = cCollider()
def Create():
	run = True
	levelCreator = CreateRECTS()
	MapInputText = Text(300,250,levelCreator.inputString,50,[0,0,0])
	while run:
		for event in pygame.event.get():
			if levelCreator.gettingInput:
				if event.type == pygame.KEYDOWN:
					levelCreator.getInput(event.type,event.key,event.unicode)
			if event.type == pygame.QUIT:
				run = False
				UI.run = False

		clock.tick()
		fps = clock.get_fps()

		levelCreator.delay -= 1/fps
		screen.fill((255,255,255))
		if levelCreator.gettingInput:
			MapInputText.render(levelCreator.inputString)
		else:
			levelCreator.cColliderObj.renderColliders()
			levelCreator.createCollider(1/fps)

		FPStext.render("FPS: "+str(round(fps)))
		pygame.display.update()

	levelCreator.dumpPickle()

def Play():
	run = True
	colliderCreator.loadPickle()
	colliderCreator.createColliders()

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				UI.run = False


		clock.tick()
		fps = clock.get_fps()

		screen.fill((255,255,255))

		colliderCreator.renderColliders()

		playerInstance.getColor()
		playerInstance.playerInputCheck()
		playerInstance.playerMove(fps)
		playerInstance.playerColission(colliderCreator.rects)
		FPStext.render("FPS: "+str(round(fps)))
		#Drawing
		#screen.blit(playerimg,playeR.collisionRect)
		pygame.display.update()

def GUI():
	Playtext = Text(64,64,"play",60,[255,255,255])
	Createtext = Text(64,144,"create",60,[255,255,255])
	while UI.run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				UI.run = False

		clock.tick()
		fps = clock.get_fps()

		screen.fill((255,255,255))

		UI.getInput()
		UI.inputCheck()
		UI.drawUI()
		Playtext.render("play")
		Createtext.render("create")
		FPStext.render("FPS: "+str(round(fps)))

		pygame.display.update()

		if UI.goToThis == 1:
			Play()
		if UI.goToThis == 2:
			Create()
GUI()

pygame.quit()

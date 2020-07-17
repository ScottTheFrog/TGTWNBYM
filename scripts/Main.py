import pygame
import playerClass
import rectClass
import random
from createColliders import cCollider
from GUI import gameUI

pygame.init()
clock = pygame.time.Clock()
#area = pygame.Surface([3000,3000])
#playerimg = pygame.image.load("Sprites/creepy.png")
screen = pygame.display.set_caption("RogueLike Game")
screen = pygame.display.set_mode([800,600])

UI = gameUI()

playerInstance = playerClass.playerObject(0,300,3,1)

#sound = pygame.mixer.Sound("sound.wav")
#sound.play()
#sound.set_volume(0.25)

colliderCreator = cCollider()
colliderCreator.loadPickle()
colliderCreator.createColliders()
def Play():
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		clock.tick()
		fps = clock.get_fps()

		screen.fill((255,255,255))

		playerInstance.getColor()
		playerInstance.playerInputCheck()
		playerInstance.playerMove(fps)
		playerInstance.playerColission(colliderCreator.rects)

		colliderCreator.renderColliders()
		#Drawing
		#screen.blit(playerimg,playeR.collisionRect)
		pygame.display.update()

def GUI():
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
		pygame.display.update()
		
		if UI.goToThis == 1:
			Play()

GUI()

pygame.quit()

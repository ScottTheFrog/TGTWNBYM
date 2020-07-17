import pygame
import playerClass
import rectClass
import random
from createColliders import cCollider

pygame.init()
run = True
clock = pygame.time.Clock()
#area = pygame.Surface([3000,3000])
#playerimg = pygame.image.load("Sprites/creepy.png")
screen = pygame.display.set_caption("RogueLike Game")
screen = pygame.display.set_mode([800,600])
playerInstance = playerClass.playerObject(0,300,3,1)

#sound = pygame.mixer.Sound("sound.wav")
#sound.play()
#sound.set_volume(0.25)
colliderCreator = cCollider()
colliderCreator.loadPickle()
colliderCreator.createColliders()
while run:
	clock.tick()
	fps = clock.get_fps()
	print(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	screen.fill((255,255,255))
	#Functions
	playerInstance.playerInputCheck()
	playerInstance.playerMove(fps)
	playerInstance.playerColission(colliderCreator.rects)
	playerInstance.getColor()
	colliderCreator.renderColliders()
	#Drawing
	#screen.blit(playerimg,playeR.collisionRect)
	pygame.display.update()
pygame.quit()

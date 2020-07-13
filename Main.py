import pygame
import playerClass
import rectClass
import random
import math
pygame.init()
run = True
clock = pygame.time.Clock()
area = pygame.Surface([3000,3000])
playerimg = pygame.image.load("Sprites/creepy.png")
screen = pygame.display.set_caption("RogueLike Game")
screen = pygame.display.set_mode([800,600])
playeR = playerClass.playerObject(0,300,3,1)

#sound = pygame.mixer.Sound("sound.wav")
#sound.play()
#sound.set_volume(0.25)
rects = {}
rectList = [rectClass.colission(200,100,200,50,[170,170,170],True,rects),
			rectClass.colission(0,125,50,100,[170,170,170],False,rects),
			rectClass.colission(0,500,800,100,[170,0,0],False,rects)
			]
rectNumber = range(0,len(rectList))
def createColliders():
	for name in rectNumber:
		rectList[name].create(rects)

while run:
	clock.tick()
	fps = clock.get_fps()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	screen.fill((255,255,255))
	#Functions
	playeR.playerInputCheck()
	playeR.playerMove(fps)
	playeR.playerColission(rects)
	createColliders()
	#Drawing
	#screen.blit(playerimg,playeR.collisionRect)
	pygame.display.update()
pygame.quit()
import pygame
import playerClass
import random
import math
pygame.init()
run = True
clock = pygame.time.Clock()
area = pygame.Surface([3000,3000])
playerimg = pygame.image.load("Sprites/creepy.png")
screen = pygame.display.set_caption("RogueLike Game")
screen = pygame.display.set_mode([800,600])
rect1 = playerClass.colission(200,100,200,50,[170,170,170],True,"richard")
rect2 = playerClass.colission(0,125,50,100,[170,170,170],False,"jhon")
rect3 = playerClass.colission(0,500,800,100,[170,0,0],False,"nigger")
playeR = playerClass.playerObject(0,300,3,1)

sound = pygame.mixer.Sound("sound.wav")
#sound.play()
sound.set_volume(0.25)
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
	playeR.playerColission()
	rect1.create()
	rect2.create()
	rect3.create()
	#Drawing
	screen.blit(playerimg,playeR.collisionRect)
	pygame.display.update()
pygame.quit()
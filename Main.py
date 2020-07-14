import pygame
import playerClass
import rectClass
import random
import pickle

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
rects = {}
rectList = []
rectNumber = range(0,len(rectList))
def createColliders():
	for name in rects:
		rectList.append(rectClass.colission(rects[name][0][0],rects[name][0][1],
								rects[name][0][2],rects[name][0][3],
								rects[name][2],
								rects[name][1],
								rects))
	for name in range(0,len(rectList)):
		rectList[name].create(rects)

print("OPENING PICKLE MAP FILE")
pickleIN = open("map1.pickle", "rb")
rects = pickle.load(pickleIN)
pickleIN.close()
while run:
	clock.tick()
	fps = clock.get_fps()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	screen.fill((255,255,255))
	#Functions
	playerInstance.playerInputCheck()
	playerInstance.playerMove(fps)
	playerInstance.playerColission(rects)
	createColliders()
	#Drawing
	#screen.blit(playerimg,playeR.collisionRect)
	pygame.display.update()
pygame.quit()
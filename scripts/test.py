import pygame
run = True
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([800,600])
while run:
	clock.tick()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				print(event.unicode)
			elif event.key == pl.K_RETURN:
				return True
	screen.fill((255,255,255))
	pygame.display.update()
pygame.quit()
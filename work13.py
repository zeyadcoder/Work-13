import pygame
pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.draw.circle(screen,(100,100,100),(200,200),(50))
pygame.draw.circle(screen, (100,100,100), (200,200), (50), (20))
done = False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT():
            done = True
pygame.quit()
import pygame

pygame.init() 

win = pygame.display.set_mode([500,500])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((255,255,255))
    pygame.draw.circle(win, (0, 0, 255), (250, 250), 75)
    pygame.draw.rect(win, (0,0,255), (100, 100,200,250))
    pygame.display.flip()
pygame.quit()

import pygame
pygame.init()  
pygame.display.set_caption("Eel")  
screen = pygame.display.set_mode((1000,1000))  
screen.fill((0,0,255))
GREEN = (255,0,0)


pygame.draw.rect(screen, (GREEN), (200,200,25,25))

pygame.display.flip()

#pygame.quit()

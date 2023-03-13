import pygame
# import sys

import subprocess
 
# Initializing Pygame
pygame.init()
 
# Initializing surface
surface = pygame.display.set_mode((600,250))
pointLists = [(300, 20), (330, 200),(100, 220)]
x =500
y = 134
pointLists.append((x,y))
run = True
while run: 
# Initializing Color
    color = (0,0,255)
    white_color = (255,255,255)
    
    # Drawing Rectangle

    # for pointList in pointLists:
    #     drawPoints = [[l[0], l[1]] for l in pointList]
    # pygame.draw.lines(surface,color,False, pointLists, 3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            run =False
        if event.type == pygame.QUIT:
            run =False
    pygame.display.update()
    print("start")
    for i in range(400000):
        pass
    print("end")
    x= (x +456 )% 600
    y= (y +241 )% 250
    pointLists.append((x,y))
    pygame.draw.polygon(surface,white_color , pointLists)

    pygame.draw.rect(surface, color, pygame.Rect(125, 0, 50, 100))
    pygame.draw.rect(surface, color, pygame.Rect(125, 150, 50, 100))
    pygame.draw.polygon(surface,color , ((300, 50), (235.04, 87.5), (235.04, 162.5), (300, 200), (364.95, 162.5), (364.95, 87.5)))
    pygame.draw.polygon(surface,color , ((460,25),(460,225),(510,125)))

    pygame.display.update()

pygame.quit()
print(pointLists)
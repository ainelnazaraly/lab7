import pygame 

pygame.init()
WIN=pygame.display.set_mode((500, 500))
pygame.display.set_caption("CIRCLE")


is_green=True
run=True
x=25
y=25

while run: 
    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            run=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE: 
            is_green=not is_green
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            run=False

    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y-=2
    if pressed[pygame.K_DOWN]: y+=2
    if pressed[pygame.K_LEFT]: x-=2
    if pressed[pygame.K_RIGHT]: x+=2
    if x+25>500: x=475
    if x-25<0: x=25
    if y+25>500: y=475
    if y-25<0: y=25


    if is_green: color=(0, 124, 55)
    else: color=(123, 67, 45)

    WIN.fill((255, 255, 255))
    pygame.draw.circle(WIN, color, (x, y), 25)
    pygame.display.flip()

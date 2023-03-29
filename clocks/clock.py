import pygame 
import datetime

pygame.init()
WIN=pygame.display.set_mode((700, 700))
pygame.display.set_caption("CLOCKS")
WIN.fill((255, 255, 255))

base=pygame.image.load('base.png')
base=pygame.transform.scale(base, (700,700))
rick=pygame.image.load('rick2.png')
rick=pygame.transform.scale(rick, (100, 400))

hand1=pygame.image.load('sechand.png')
#hand1=pygame.transform.scale(hand1, (120, 400))

hand2=pygame.image.load('minhand.png')
#hand2=pygame.transform.scale(hand2, (120,400))

run=True
clock=pygame.time.Clock()

def rotate(sf, tm): 
    sf1=pygame.transform.rotate(sf, tm)
    sf1rec=sf1.get_rect(center=(350, 350))
    WIN.blit(sf1, sf1rec)


while run: 
    crtm=datetime.datetime.now()
    sec=crtm.second
    min=crtm.minute
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            run=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            run=False
    
    WIN.blit(base, (0,0))
    WIN.blit(rick, (300,150))

    rotate(hand1, -1*(sec*6))
    rotate(hand2, -1*(min*6))
    '''hand11=pygame.transform.rotate(hand1, -1*((6*sec))+90)
    hand12=hand11.get_rect(center=(335, 350))
    #hand12.center=hand1_rect.center
    WIN.blit()


    hand21=pygame.transform.rotate(hand2, -1*((6*min))-180)
    hand22=hand21.get_rect(center=(350, 350))
    #hand22.center=hand2_rect.center
    WIN.blit()'''
    
    clock.tick(60)
    pygame.display.flip()

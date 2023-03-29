import pygame
import os 
from pygame import mixer 

pygame.init()
mixer.init()
WIN=pygame.display.set_mode((400, 300))
pygame.display.set_caption("PLAYER")
WIN.fill((255, 255, 255))

run=True
check=True

base=pygame.image.load('play.png')
base=pygame.transform.scale(base, (400, 300))
sg=[]
path="/Users/ainelnazaraly/Documents/python/lab7/musicplayer"
files=os.listdir(path)
for i in files: 
    if i.endswith('.mp3'): 
        sg.append(i)

cur=0
cs=pygame.mixer.music.load(sg[cur])
pygame.mixer.music.play()
pygame.mixer.music.pause()

font=pygame.font.SysFont('arial',17, True )

while run: 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            run=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
            run=False

        if event.type==pygame.KEYDOWN: 
            if event.key==pygame.K_SPACE:
                if check:
                    pygame.mixer.music.unpause()
                    check=False 
                else: 
                    pygame.mixer.music.pause()
                    check=True

            if event.key==pygame.K_RIGHT: 
                if cur<len(sg)-1: 
                    pygame.mixer.music.stop()
                    cur+=1
                    pygame.mixer.music.load(sg[cur])
                    pygame.mixer.music.play()
                else:
                    cur=0
                    pygame.mixer.music.load(sg[cur])
                    pygame.mixer.music.play() 
                
            if event.key==pygame.K_LEFT: 
                if cur>0: 
                    cur-=1
                    pygame.mixer.music.load(sg[cur])
                    pygame.mixer.music.play()
                else:
                    cur=len(sg)-1
                    pygame.mixer.music.load(sg[cur])
                    pygame.mixer.music.play()
                    
            
    WIN.blit(base, (0, 0))

    sgf=sg[cur]
    sgnm=sgf.replace(".mp3", "")

    text=font.render(sgnm, True, (0, 0, 0))
    WIN.blit(text, (110, 80))

    pygame.display.flip()


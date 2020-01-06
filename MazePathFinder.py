
import pygame
# generate random integer values
from random import seed
from random import randint
# seed random number generator



pygame.init()
win=pygame.display.set_mode((600,600))
pygame.display.set_caption("Breadth First Search")
win.fill((255, 255, 255))

width=600
height=600
h=0
w=0
x=0
y=0
run=True

queue=[]
queue.append((x, y))        
marked=False


def bfs():
    dist=0
    tx=0
    ty=0
    while True:
        if not queue:
            break
        s=len(queue)
        while(s>0):
            l=queue.pop(0)
            tx=l[0]
            ty=l[1]
            if(tx==590 and ty==590):
                print('true '+str(dist+20))
                return
            if(l[0]-10>=0):
                if(win.get_at((l[0]-10, l[1]))[0]==20):
                    queue.append((l[0]-10, l[1]))
                    pygame.draw.rect(win, (255, 0, 0), (l[0]-10, l[1], 10, 10))
                    pygame.display.update()
            if(l[1]-10>=0):
                if(win.get_at((l[0], l[1]-10))[0]==20):
                    queue.append((l[0], l[1]-10))
                    pygame.draw.rect(win, (255, 0, 0), (l[0], l[1]-10, 10, 10))
                    pygame.display.update()

            if(l[0]+10<600):
                if(win.get_at((l[0]+10, l[1]))[0]==20):
                    queue.append((l[0]+10, l[1]))
                    pygame.draw.rect(win, (255, 0, 0), (l[0]+10, l[1], 10, 10))
                    pygame.display.update()
            if(l[1]+10<600):
                if(win.get_at((l[0], l[1]+10))[0]==20):
                    queue.append((l[0], l[1]+10))
                    pygame.draw.rect(win, (255, 0, 0), (l[0], l[1]+10, 10, 10))
                    pygame.display.update()

            s=s-1
        dist+=10
    print('false')


def obstacles():
    o=0
    recx=0
    recy=0
    while o<80:
        recx=(int)((randint(0, width)/10))*10
        recy=(int)((randint(0, height)/10))*10
        pygame.draw.rect(win, (0, 0, 0), (recx, recy, 10, 10))
        pygame.display.update()
        marked=True
        o+=1
    pygame.draw.rect(win, (0, 0, 0), (10, 0, 10, 10))

#main loop
while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             run=False
    while h<=height:
        pygame.draw.line(win, (20, 0, 0), (h, 0), (h, width))
        h+=10
        pygame.display.update()
    while w<=width:
        pygame.draw.line(win, (20, 0, 0), (0, w), (height, w))
        w+=10
        pygame.display.update()
    while (marked==False):
        obstacles()
        marked=True
    if(marked==True):
        bfs()
    break    


pygame.quit()

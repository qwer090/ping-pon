from pygame import *
from random import choice
window = display.set_mode((700,500))
display.set_caption('пинг пон')
background = transform.scale(image.load('les2.jpg'),(700,500))



class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__()
        self.image  = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.speed=speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 
    def collidepoint (self,x,y):
        return self.rect.collidepoint(x,y)    


class Player(GameSprite):
    def updateL(self):
        keys= key.get_pressed()
        if keys[K_d]and self .rect.y >10:
            self.rect.y -=self.speed
        if keys[K_a]and self .rect.y <500-10-self.rect.height:
            self.rect.y +=self.speed    

class Player1(GameSprite):
    def updateR(self):
        keys= key.get_pressed()
        if keys[K_LEFT]and self .rect.y >10:
            self.rect.y -=self.speed
        if keys[K_RIGHT]and self .rect.y <500-10-self.rect.height:
            self.rect.y +=self.speed               

class Bool(GameSprite):
    def __init__(self,img,x,y,w,h,speed):
        super().__init__(img,x,y,w,h,speed)
        self.direct  = [0,0]
        
    def update(self):
        global skore_l,skore_r
        self.rect.x += self.speed*self.direct[0]
        self.rect.y += self.speed*self.direct[1]
        if self.rect.y<=0 or self.rect.y>=500-self.rect.height:
            self.direct[1]*= -1
        #if self.rect.x<=0 or self.rect.x>=700-self.rect.width:
            #self.direct[0]*= -1
        if self.rect.colliderect(pl_l) or self.rect.colliderect(pl_r):
            self.direct[0]*=-1    
        if self.rect.x<=0:
            skore_r +=1
            self.start()
        if self.rect.x>=700-self.rect.width:
            skore_l +=1
            self.start()


    def start(self):  
        self.rect.y=225 
        self.rect.x=325 
        bool.direct[0] = choice([-1,1])
        bool.direct[1] = choice([-1,1])
          




bool = Bool('valan-Photoroom.png',350-25,250-25,50,50,5)
bool.direct[0] = choice([-1,1])
bool.direct[1] = choice([-1,1])
pl_l = Player('Rarenrf-Photoroom.png',0,400,100,100,5)
pl_r = Player1('Rarenrf-Photoroom.png',600,400,100,100,5)
#музыка
mixer.init()
mixer.music.load('muz.mp3')
mixer.music.play()


game = True
skore_r = 0
skore_l = 0
rule= 3
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
       
  

    window.blit(background,(0,0))
    pl_l.updateL()
    pl_l.reset()
    pl_r.updateR()
    pl_r.reset()
    bool.update()
    bool.reset()
    display.update()  
    clock.tick(FPS)          

from pygame import *
window = display.set_mode((700,500))
display.set_caption('пинг пон')
background = transform.scale(image.load('ojpoi.jpg'),(700,500))



#задай фон сцены




#музыка
mixer.init()
mixer.music.load('muz.mp3')
mixer.music.play()


game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
       
  

    window.blit(background,(0,0))
    display.update()  
    clock.tick(FPS)          

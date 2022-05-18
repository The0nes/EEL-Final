import pygame
import random
import math
pygame.init()  
pygame.display.set_caption("EEL")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
doExit = False
end = False
red = (255,0,0)


Eel = pygame.image.load('eelface.png') #load your spritesheet
Eel.set_colorkey((255,255,255))
EelB = pygame.image.load('eelbody.png') #load your spritesheet
EelB.set_colorkey((255,255,255))
Eel2 = pygame.image.load('eelface2.png') #load your spritesheet
Eel2.set_colorkey((255,255,255))
# EelB2 = pygame.image.load('eelbody2.png') #load your spritesheet
# EelB2.set_colorkey((255,255,255))

fishy = pygame.image.load('fishy.png')
fishy.set_colorkey((255,255,255))
Back = pygame.image.load('background.png')

eat = pygame.mixer.Sound('nom.wav')


#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
Px= 800 #xpos of player
Py= 800 #ypos of player
Px2 = 200
Py2 = 200
score = 0
score2 = 0
vx = 0 #x velocity of player
vy = 0 #y velocity of player
vx2 = 0
vy2 = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed
second = [False, False, False, False]

tailSize = 0
tailSize2 = 0
counter = 0

frameWidth = 50
frameHeight = 50
RowNum = 2
frameNum = 0
RowNum2 = 0
frameNum2 = 0
RowNum3 = 0
frameNum3 = 0

tailX = []
tailY = []
tailX2 = []
tailY2= []

def CircleCollision(x1,x2,y1,y2, radius):
    if (math.sqrt((x2 - x1)**2 + (y2- y1)**2))<radius:
        return True
    else:
        return False

#set up first circle's position and color and size
num = random.randrange(1, 800)
num1 = random.randrange(1, 800)
c1 = random.randrange(1, 255)
c2 = random.randrange(1, 255)
c3 = random.randrange(1, 255)
s = 25
#set up variable to hold mouse position
xpos=0
ypos=0
mousePos = (xpos, ypos)


while not doExit: #GAME LOOP############################################################
    clock.tick(60) #FPS

#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()    


#Input Section------------------------------------------------------------

    if event.type == pygame.MOUSEBUTTONDOWN:#CLICK
        mousePos = event.pos


    if event.type == pygame.QUIT: #close game window
        break        
  
    #physics section-----------------------------------------
    if mousePos[0] > 133 and mousePos[0] < 233 and mousePos[1] > 439 and mousePos[1] < 489:
        n = 3
        doExit= True
    if mousePos[0] > 437 and mousePos[0] < 537 and mousePos[1] > 439 and mousePos[1] < 489:
        n = 5
        doExit= True
    if mousePos[0] > 767 and mousePos[0] < 867 and mousePos[1] > 439 and mousePos[1] < 489:
        n = 10
        doExit= True
    if mousePos[0] > 233 and mousePos[0] < 723 and mousePos[1] > 639 and mousePos[1] < 689:
        n = 50
        doExit= True
    print(mousePos)
    #Render Section ---------------------------
    screen.fill((0,0,0)) #wipes screen black
    pygame.draw.rect(screen, (0, 255, 255), (133,439, 100, 50))
    pygame.draw.rect(screen, (255, 255, 0), (437,439, 100, 50))
    pygame.draw.rect(screen, (0, 255, 0), (767,439, 100, 50))
    pygame.draw.rect(screen, (255, 0, 0), (233,639, 490, 50))
    font = pygame.font.Font(None, 65)
    text = font.render(str("How fast would you like to go?"),1, (255,255,255))
    screen.blit(text, (200,250))
    text = font.render(str("slow"),1, (0, 250, 250))
    screen.blit(text, (133,390))
    text = font.render(str("normal"),1, (250, 250, 0))
    screen.blit(text, (415,390))
    text = font.render(str("fast"),1, (0, 250, 0))
    screen.blit(text, (778,390))
    text = font.render(str("extrememe"),1, (250, 0, 0))
    screen.blit(text, (360,590))
    pygame.display.flip()  

pygame.quit()

import pygame
import random
import math
pygame.init()  
pygame.display.set_caption("EEL")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
musica = pygame.mixer.music.load('musica.wav')
pygame.mixer.music.play(-1)

while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    counter += 1
    if n == 3:
        if counter > 18:
            counter =0
            tailX.insert(0,Px)
            tailY.insert(0,Py)
            tailX2.insert(0,Px2)
            tailY2.insert(0,Py2)
    if n == 5:
        if counter > 10:
            counter = 0
            tailX.insert(0,Px)
            tailY.insert(0,Py)
            tailX2.insert(0,Px2)
            tailY2.insert(0,Py2)
    if n == 10:
        if counter > 5:
            counter = 0
            tailX.insert(0,Px);
            tailY.insert(0,Py)
            tailX2.insert(0,Px2)
            tailY2.insert(0,Py2)
    if n == 50:
        if counter > 2:
            counter = 0
            tailX.insert(0,Px)
            tailY.insert(0,Py)
            tailX2.insert(0,Px2)
            tailY2.insert(0,Py2)
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)


#Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=True
            if event.key == pygame.K_a:
                second[LEFT]=True
            elif event.key == pygame.K_d:
                second[RIGHT]=True
            elif event.key == pygame.K_w:
                second[UP]=True
            elif event.key == pygame.K_s:
                second[DOWN]=True
           
        if event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_DOWN:
                keys[DOWN]=False
            if event.key == pygame.K_a:
                second[LEFT]=False
            elif event.key == pygame.K_d:
                second[RIGHT]=False
            elif event.key == pygame.K_w:
                second[UP]=False
            elif event.key == pygame.K_s:
                second[DOWN]=False
                
    
    
    #physics section--------------------------------------------------------------------
    
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-n
        vy=0
        RowNum = 2
        frameNum = 0
        direction = LEFT
        
    #Right Movement
    elif keys[RIGHT]==True:
        vx=n
        vy=0
        RowNum = 0
        frameNum = 0
        direction = RIGHT
    
      #JUMPING  
    if keys[UP]==True:
        vy=-n
        vx=0
        RowNum = 1
        frameNum = 0
        direction = UP
        
      #DOWN
    if keys[DOWN]==True:
        vy=+n
        vx=0
        RowNum = 3
        frameNum = 0
        direction = DOWN
    
    #LEFT MOVEMENT
    if second[LEFT]==True:
        vx2=-n
        vy2=0
        RowNum2 = 2
        frameNum2 = 0
        direction2 = LEFT
        
    #Right Movement
    elif second[RIGHT]==True:
        vx2=n
        vy2=0
        RowNum2 = 0
        frameNum2 = 0
        direction2 = RIGHT
    
      #JUMPING  
    if second[UP]==True:
        vy2=-n
        vx2=0
        RowNum2 = 1
        frameNum2 = 0
        direction2 = UP
        
      #DOWN
    if second[DOWN]==True:
        vy2=+n
        vx2=0
        RowNum2 = 3
        frameNum2 = 0
        direction2 = DOWN
    #update player position
    Px+=vx 
    Py+=vy
    Px2+=vx2
    Py2+=vy2
    
    #try to call the function here, use the new variables
    #(put the call inside an if statement, and only get new points for the circle when it's clicked on)
    if CircleCollision(num+25,Px+25, Py,num1+5, s)==True:
        num = random.randrange(1, 800)
        num1 = random.randrange(1, 800)
        c1 = random.randrange(1, 255)
        c2 = random.randrange(1, 255)
        c3 = random.randrange(1, 255)
        s = 25
        pygame.mixer.Sound.play(eat)
        frameNum += 1
        tailSize += 1
        score += 1
        
    elif CircleCollision(num+ 25,Px2+20, Py2,num1+5, s)==True:
        num = random.randrange(1, 800)
        num1 = random.randrange(1, 800)
        c1 = random.randrange(1, 255)
        c2 = random.randrange(1, 255)
        c3 = random.randrange(1, 255)
        s = 25
        pygame.mixer.Sound.play(eat)
        frameNum2 += 1
        tailSize2 += 1
        score2 += 1
#player 1 warp zone
    if Px < 0:
        Px=999
    if Px > 999:
        Px=0
    if Py < 0:
        Py=999
    if Py > 999:
        Py=0
#player 2 warp zone        
    if Px2 < 0:
        Px2=999
    if Px2 > 999:
        Px2=0
    if Py2 < 0:
        Py2=999
    if Py2 > 999:
        Py2=0
#player collision
    if Px > Px2 and Px < Px2 + 50 and Py > Py2 and Py < Py2 + 50:
        score = 0
        score2 = 0
        Px2 = 200
        Py2 = 200
        Px = 800
        Py = 800
        vx = 0
        vy = 0
        vx2 = 0
        vy2 = 0
        tailSize = 0
        tailSize2 = 0
    if Px2 > Px and Px2 < Px + 50 and Py2 > Py and Py2 < Py + 50:
        score = 0
        score2 = 0
        Px2 = 200
        Py2 = 200
        Px = 800
        Py = 800
        vx = 0
        vy = 0
        vx2 = 0
        vy2 = 0
        tailSize = 0
        tailSize2 = 0
    if score >= 20:
        gameover = True
    if score2 >= 20:
        gameover = True
    #Render Section ---------------------------
    screen.fill((0,0,255))
    screen.blit(Back, (0,0), (0,0,1000,1000))
    font = pygame.font.Font(None, 74)
    text = font.render(str(score),1, (0, 255, 0))
    screen.blit(text, (750, 10))
    text = font.render(str(score2),1, (0, 255, 0))
    screen.blit(text, (250, 10))
    screen.blit(fishy,(num, num1,20,20))
    for i in range (0, tailSize):
      pygame.draw.rect(screen, (255,228,141), (tailX[i], tailY[i], 50, 50))
      #screen.blit(EelB, (tailX[i], tailY[i], frameWidth, frameHeight))
    screen.blit(Eel, (Px, Py), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    for i in range (0, tailSize2):
      pygame.draw.rect(screen, (83,83, 255), (tailX2[i], tailY2[i], 50, 50))
    screen.blit(Eel2, (Px2, Py2), (frameWidth*frameNum2, RowNum2*frameHeight, frameWidth, frameHeight))    

    pygame.display.flip()

pygame.quit()

import pygame
import random
import math
pygame.init()  
pygame.display.set_caption("EEL")  # sets the window title
screen = pygame.display.set_mode((1000, 1000))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock

while not end:
    screen.fill((0,0,255))
    if score >= 20:
        font = pygame.font.Font(None, 65)
        text = font.render(str("GAME OVER"),1, (255,255,255))
        screen.blit(text, (200,250))
        text = font.render(str("Player 2 wins!"),1, (250, 250, 0))
        screen.blit(text, (415,390))
    if score2 >= 20:
        font = pygame.font.Font(None, 65)
        text = font.render(str("GAME OVER"),1, (255,255,255))
        screen.blit(text, (200,250))
        text = font.render(str("Player 1 wins!"),1, (250, 250, 0))
        screen.blit(text, (415,390))
    pygame.display.flip()
pygame.quit()

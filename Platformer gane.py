
from turtle import st
import pygame
import sys
import os

current_dir=os.getcwd()#gets current working directory
print(current_dir)
os.chdir("C:\VsCode\Platformer game")#changes working directory to the correct folder
print(os.getcwd())

pygame.init()
Increase_Downward_velocity=pygame.USEREVENT+1#creates a custom event add plus whatever number of event it is to create multipl
Moveleft=pygame.USEREVENT+2
MoveRight=pygame.USEREVENT+3
MoveUp=pygame.USEREVENT+4
screenHeight=(1080)
screenWidth=(1920)
background=pygame.image.load("Game.png")
Green=(0,255,0)
HealthbarWidth=100
screen=pygame.display.set_mode((screenWidth,screenHeight),pygame.RESIZABLE)
clock=pygame.time.Clock()
    
#creating floor rect 
Ground=pygame.Rect(0,825,screenWidth,500)#defines Ground width and height along with spawning coordinates

Direction="right"#starts off having character face right
class Character(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,DownwardVelocity,Xvelocity):#Assigns arguments to class using __init__ all velocity calculations done within the character class so all characters inherit velocity
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image=pygame.image.load("Goblin Defualt-Right.png")
        self.rect=self.image.get_rect()                      
        self.rect.center = [pos_x,pos_y]#tells center of the rect to follow postion x and y
        self.DownwardVelocity=9.8
        self.Xvelocity=3
        self.health=100 

    def RightJump(self):
        self.rect.x-=self.Xvelocity#gives jumps momentum by adding Xvelocity to the jump
        for i in range (20):
            self.rect.y-=self.Xvelocity
        self.DownwardVelocity=9.8
    
    def LeftJump(self):
        self.rect.x+=self.Xvelocity#gives jumps momentum by adding Xvelocity to the jump
        for i in range (20):
            self.rect.y-=2
        self.DownwardVelocity=9.8 

    def Jump(self):
        for i in range (20):
            self.rect.y-=2
        self.DownwardVelocity=9.8

    def superJump(self):#moves up by increments of 1 so it looks smoothe
        self.rect.x+=self.Xvelocity#gives jumps momentum by adding Xvelocity to the jump
        for i in range (100):
            self.rect.y-=1
        self.DownwardVelocity=9.8

    def updateLeft(self):
            self.rect.x-=2
            pygame.time.set_timer(Moveleft,1)#Uses custom events and timers because it looks smoother than a for loop
          
    def updateRight(self):
            self.rect.x+=2
            pygame.time.set_timer(MoveRight,1)
        
      
    def Vertical_vel(self):
        self.rect.y+=self.DownwardVelocity

    def collisionFloor(self):
        if self.rect.colliderect(Ground): 
            self.DownwardVelocity=0    


    def Falling(self):
        global Direction
        if self.rect.colliderect(Ground)==False and self.DownwardVelocity==9.8 and Direction=="left":# gravity goes way you are moving to stop movement inconsistency
            pygame.time.set_timer(Increase_Downward_velocity,1000)
            self.rect.x+=self.Xvelocity

        if self.rect.colliderect(Ground)== False and self.DownwardVelocity==9.8 and Direction=="right":
            pygame.time.set_timer(Increase_Downward_velocity,1000)
            self.rect.x-=self.Xvelocity
        
    def DownwardVelocitySquared(self):
        self.DownwardVelocity=self.DownwardVelocity*self.DownwardVelocity 
    
    def Movey(self):
        self.rect.y+=2

    def MoveXleft(self):
        self.rect.x-=2

class Steve(Character):#creates a subclass for steve
        def __init__(self, width, height, pos_x, pos_y,DownwardVelocity,Xvelocity):
            super().__init__(width, height, pos_x, pos_y,DownwardVelocity,Xvelocity)
            self.sprites=[]
           
               
        def collision(self):
            if pygame.sprite.groupcollide(Steve_group,Enemy_group,False,False):#groupcollide(group1,group2,Dokill(means if hits something it disappears can either be true or fals)group1,dokill group2)
                self.takeDamage()
                self.rect.x+=self.Xvelocity
                #doing x and y seperately makes it look more natural
                for i in range(120):
                    self.rect.x-=2

                for i in range(60):
                    self.rect.y-=2
                self.DownwardVelocity=9.8
        
        def takeDamage(self):
            global HealthbarWidth
            self.health-=10
            HealthbarWidth-=10
            if self.health <=0:
                self.kill()

class Enemy(Character):#inherits characteristics of the parent class character
    def __init__(self, width, height, pos_x, pos_y,DownwardVelocity,Xvelocity):
        super().__init__(width, height, pos_x, pos_y,DownwardVelocity,Xvelocity)#calls arguments from parent class 
        self.image=="Enemy1.png"
    def talk(self):
        print("working")

    
        
steve=Steve(10,10,screenWidth/2,screenHeight/2,9.8,3)#creates an instance of the steve class and defines values for arguments

E=Enemy(10,10,screenWidth,screenHeight/2,9.8,3)

#making an instance of class with arguments NOTE CANNOT DRAW SPRITES INDIVUALLY HAVE TO GROUP THEM

Steve_group=pygame.sprite.Group() 
Enemy_group=pygame.sprite.Group()
#adds sprites to groups
Steve_group.add(steve)
Enemy_group.add(E)

while True:
    Healthbar=pygame.Rect(10,10,HealthbarWidth,20)#healthbar is here so it can constantly check what healthbar is so i can update its width
    print(steve.health)
    Pressed=pygame.key.get_pressed()
    Stevex=steve.rect.x
    pygame.init()
    steve.Vertical_vel()
    E.Vertical_vel()
    x,y=screen.get_size()
    #Downward and upward velocity functions for every sprite
    steve.collisionFloor() 
    steve.Falling()
    E.collisionFloor()
    steve.collision()
    E.Falling() 
    for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if pygame.event.get(Moveleft):
                self.rect.x+=2

            if pygame.event.get(MoveRight):
                self.rect.x-=2

                
            if pygame.event.get(Increase_Downward_velocity):
                steve.DownwardVelocitySquared()
                                                                                                                                
            if Pressed[pygame.K_LEFT]or Pressed[pygame.K_a]:
                steve.updateLeft()
                Direction="left"#direction that x of gravity will go in so Xvelocity doesnt interfere with left and right movement
                
            if Pressed[pygame.K_1] and steve.rect.colliderect(Ground)==True:
                steve.superJump()

            if Pressed[pygame.K_RIGHT] or Pressed[pygame.K_d]:
                steve.updateRight()
                Direction="right"

            if Pressed[pygame.K_SPACE] and Pressed[pygame.K_a] and steve.rect.colliderect(Ground)==True:
                steve.LeftJump()
            

            if Pressed[pygame.K_SPACE] and Pressed[pygame.K_d] and steve.rect.colliderect(Ground)==True:
                steve.RightJump()

            if Pressed[pygame.K_SPACE] and steve.rect.colliderect(Ground)==True:
                steve.Jump()
     

    pygame.display.flip()
    screen.blit(background,(0,0))#draws background at coordinates 0,0 on screen
    Steve_group.draw(screen)#dont need spawning coordinates because they are already defined
    Enemy_group.draw(screen)
    pygame.draw.rect(screen,Green,Healthbar)
    clock.tick(60)#sets frame rate

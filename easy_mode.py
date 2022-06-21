import pygame
from random import randint
import random
import time

global d
d = 0 
pygame.init()
pa = pygame.display.set_mode((800,900))
pa.fill((0, 0, 0))

class player:
    def __init__(self, xpos, ypos, a):
        self.xpos=xpos
        self.ypos=ypos
        self.a=a
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.a=0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.xpos=self.xpos+25
            if self.xpos>775:
                self.xpos=0
        if keys[pygame.K_LEFT]:         
            self.xpos=self.xpos-25
            if self.xpos<0:
                self.xpos=775
    def shoot(self):
        for i in bullets:
            if i.a==1:
                i.move()
                pa.blit(pygame.image.load("bul.png"), (i.xpos, i.ypos))
        if timer%2==0:#red za bullet_spawn_rate 
            for j in bullets:
                if j.a==0:
                    j.xpos=self.xpos
                    j.a=1
                    pa.blit(pygame.image.load("bul.png"), (j.xpos, j.ypos))
                    break
    def spawn(self):
        for j in enemies:
            if j.a==0:
                if j.c==0:
                    pa.blit(pygame.image.load("rock.png"), (j.xpos, j.ypos))
                    j.a=1
                if j.c==1:
                    pa.blit(pygame.image.load("bot.png"), (j.xpos, j.ypos))
                    j.a=1
                if j.c==2:
                    pa.blit(pygame.image.load("snake.png"), (j.xpos,j.ypos))
                    j.a=1
                break
        
                


class bullet:
    def __init__(self, xpos, ypos, a):
        self.xpos=xpos
        self.ypos=ypos
        self.a=a
    def move(self):
        self.ypos=self.ypos-25
    def away(self):
        if self.ypos<0:
            self.ypos=850
            self.a=0
        
class stone:
    def __init__(self, xpos, ypos, a, c, s):
        self.xpos=xpos
        self.s=s
        self.c=c
        self.ypos=ypos
        self.a=a
    def die(self):
        for i in bullets:
            if i.a==1:
                if i.xpos<self.xpos+15 and i.xpos>self.xpos-15 and i.ypos < self.ypos+15 and i.ypos>self.ypos -15:
                    i.a=0
                    i.ypos=850
                    self.a=0
                    self.ypos=0
                    d = 1
                    print("stone killed")
    def kill(self, player):
        if self.ypos==player.ypos:
            player.a=0
    def move(self):
        if timer%2==0: 
            self.ypos=self.ypos+25
        if self.s==0:
            pa.blit(pygame.image.load("rock.png"),(self.xpos, self.ypos))
        elif self.s==1:
            pa.blit(pygame.image.load("rock1.png"),(self.xpos, self.ypos))
        elif self.s==2:
            pa.blit(pygame.image.load("rock2.png"),(self.xpos, self.ypos))

class bot:
    def __init__(self, xpos, ypos, a, c, s):
        self.xpos=xpos
        self.c=c
        self.s=s
        self.ypos=ypos
        self.a=a
    def die(self):
        for i in bullets:
            if i.a==1:
                if i.xpos<self.xpos+15 and i.xpos>self.xpos-15 and i.ypos < self.ypos+15 and i.ypos>self.ypos -15:
                    i.a=0
                    i.ypos=850
                    self.a=0
                    self.ypos=0
                    d = 1
                    print("bot killed")
    def kill(self, player):
        if self.ypos==player.ypos:
            player.a=0
    def move(self):
        if timer%2==0:
            i=random.randint(0,3)
            if i==1:
                self.ypos=self.ypos+25     
            if i==0:
                self.xpos=self.xpos-25
                if self.xpos<0:
                    self.xpos=775
            if i==2:
                self.xpos=self.xpos+25
                if self.xpos>775:
                    self.xpos=0
        if self.s==0:
            pa.blit(pygame.image.load("bot.png"),(self.xpos, self.ypos))
        elif self.s==1:
            pa.blit(pygame.image.load("bot1.png"),(self.xpos, self.ypos))
        elif self.s==2:
            pa.blit(pygame.image.load("bot2.png"),(self.xpos, self.ypos))
class snake:
    def __init__(self, xpos, ypos, a, c, s):
        self.xpos=xpos
        self.c=c
        self.s=s
        self.ypos=ypos
        self.a=a
    def die(self):
        for i in bullets:
            if i.a==1:
                if i.xpos<self.xpos+15 and i.xpos>self.xpos-15 and i.ypos < self.ypos+15 and i.ypos>self.ypos -15:
                    i.a=0
                    i.ypos=850
                    self.a=0
                    self.ypos=0
                    d = 1
                    print("snake killed")
    def kill(self, player):
        if self.ypos==player.ypos:
            player.a=0
    def move(self):
        i=random.randint(0,3)    
        if timer%5==0:
            if i==0:
                self.xpos=self.xpos-25
                if self.xpos<0:
                    self.xpos=775
            if i==2:
                self.xpos=self.xpos+25
                if self.xpos>775:
                    self.xpos=0
        if timer%3!=1:
            self.ypos=self.ypos+25
        if self.s==0:
            pa.blit(pygame.image.load("snake.png"),(self.xpos, self.ypos))
        if self.s==1:
            pa.blit(pygame.image.load("snake1.png"),(self.xpos, self.ypos))
        if self.s==2:
            pa.blit(pygame.image.load("snake2.png"),(self.xpos, self.ypos))
pal=player(375, 875, 1)

enemies=[]
for i in range (500):
    c = random.randint(0, 2)
    y = random.randint(0, 31)
    l = random.randint(0, 2)
    if c==0:
        i=stone(y*25, 0, 0, c, l)
        enemies.append(i)
    if c==1:
        i=bot(y*25, 0, 0, c, l)
        enemies.append(i)
    if c==2:
        i=snake(y*25, 0, 0, c, l)
        enemies.append(i)

bullets=[]
for i in range (200):
    i=bullet(0, 850, 0)
    bullets.append(i)
timer=0
mer=50
a=stone(375, 0, 1, 0, 2)
enemies.append(a)
    
while pal.a==1:
    pa.fill((0, 0, 0))
    pygame.time.delay(100)
    pa.blit(pygame.image.load("aaa.png"), (pal.xpos, pal.ypos))
    pal.move()
    pal.shoot()
    for i in bullets:
        if i.a==1:
            i.away()
    for j in enemies:
        if j.a==1:
            j.die()
            j.move()
            j.kill(pal)
            if d == 1:
                enemies.remove(j)
                print("d=0")
                d = 0
    if timer%mer==0:
        pal.spawn()
        #if mer>1:
            #mer=mer-1
    pygame.display.update()
    timer=timer+1
    
k = random.randint(0, 3)
if k==0:
    print ("you lost, cry moar")
elif k==1:
    print("i would say you did well, but computers don't lie")
elif k==2:
    print ("try again , i love watching you fail")
elif k==3:
    print ("only you are this bad, are you ok?")

time.sleep(10)

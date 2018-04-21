#!/usr/bin/python3.5

from time import sleep
from random import randint
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Python game")


walkRight = [pygame.image.load('right1.jpg')
             , pygame.image.load('right2.jpg')
             , pygame.image.load('right3.jpg')
             , pygame.image.load('right4.jpg')
             , pygame.image.load('right5.jpg')
             , pygame.image.load('right6.jpg')
             ]

walkLeft = [pygame.image.load('left1.jpg')
            , pygame.image.load('left2.jpg')
            , pygame.image.load('left3.jpg')
            , pygame.image.load('left4.jpg')
            , pygame.image.load('left5.jpg')
            , pygame.image.load('left6.jpg')
            ]

playerStamd = pygame.image.load('trump.jpg')

bg = pygame.image.load('fon.jpg')
x = 50
y = 425
width = 50
height = 60
speed = 5


isJump = False
jumpCount = 10


left = False
right = False
animCount = 0
lastMove = 'right'

clock = pygame.time.Clock()
run = True
bullets = []
crips = []


class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y


class crip():
    def __init__(self, x, y, width, height, color, thickness):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.thickness = thickness

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width
                                           , self.height)
                         , self.thickness)


class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def drawWindow():
    win.blit(bg, (0, 0))

    global animCount
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStamd, (x, y))
    for bullet in bullets:
        bullet.draw(win)
    for crip in crips:
        crip.draw(win)

    pygame.display.update()


while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        crips.append(crip(250, 425, 60, 71, (randint(1, 255)
                                             , randint(1, 255)
                                             , randint(1, 255)),
                          5))
    if keys[pygame.K_f]:
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 2)
                                   , round(y + height // 2)
                                   , 5, (randint(1, 255)
                                         , randint(1, 255)
                                         , randint(1, 255))
                                   , facing))
        # sleep(0.1)
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
        lastMove = 'right'
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount > 0:
                y -= (jumpCount ** 2) / 2
            else:
                y += (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()
pygame.quit()

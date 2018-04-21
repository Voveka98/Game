import pygame
from Load_pictures import walkLeft
from Load_pictures import walkRight
from Load_pictures import stay_picture
from Shell import shell

picture = None
animCount = 0
WIDTH = 60
HEIGHT = 71
MOVE_SPEED = 3
lastMove = None
onGround = False
jumpCount = 10



class player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.x = x
        self.y = y
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.stay_picture = stay_picture
        self.lastMove = lastMove
        self.image = pygame.image.load('/home/vovek/PythonGame/assets/trump.jpg')
        self.rect = self.image.get_rect()
        self.onGround = onGround
        self.jumpCount = jumpCount

    def motion(self):
        global animCount
        global picture
        if animCount + 1 >= 30:
            animCount = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 5:
            animCount += 1
            self.image = self.walkRight[animCount // 5]
            self.x -= MOVE_SPEED
            self.lastMove = 'left'

        elif (keys[pygame.K_RIGHT] and self.x < 450):
            animCount += 1
            self.image = self.walkLeft[animCount // 5]
            self.x += MOVE_SPEED
            self.lastMove = 'right'

        else:
            self.image = self.stay_picture

        if self.onGround:
            if (keys[pygame.K_UP] or keys[pygame.K_SPACE]):
                self.onGround = False
        else:
            if self.jumpCount >= -10:
                if self.jumpCount > 0:
                    self.y -= (self.jumpCount ** 2) / 2
                else:
                    self.y += (self.jumpCount ** 2) / 2
                self.jumpCount -= 1
            else:
                self.onGround = True
                self.jumpCount = 10

    # def fire(self, shells):
    #     for shell in shells:
    #         if self.lastMove == 'right':
    #             shell.facing = 1
    #             shell.draw()

    def collide(self, xvel, yvel, blocks):
        for p in blocks:
            if pygame.sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

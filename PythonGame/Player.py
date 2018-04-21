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
        self.xvel_to_right = MOVE_SPEED
        self.xvel_to_left = MOVE_SPEED
        self.yvel = MOVE_SPEED
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = y
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.stay_picture = stay_picture
        self.lastMove = lastMove
        self.image = pygame.image.load('assets/trump.jpg')
        self.rect = self.image.get_rect()
        self.onGround = onGround
        self.jumpCount = jumpCount

    def collide(self, blocks):
        for block in blocks:
            if (self.x > block.x and self.x < block.x + block.Blocks_Width and
                ((self.y > block.y and self.y < block.y + block.Blocks_Height) or
                 (self.y + self.HEIGHT > block.y and
                  self.y + self.HEIGHT < block.y + block.Blocks_Height))):
                self.xvel_to_left = 0
                self.xvel_to_right = MOVE_SPEED
                return [int(self.xvel_to_left), int(self.xvel_to_right)]  # то не движется вправо
            if (self.x + self.WIDTH > block.x and
                self.x + self.WIDTH < block.x + block.Blocks_Width and
                ((self.y > block.y and self.y < block.y + block.Blocks_Height) or
                 (self.y + self.HEIGHT > block.y and
                  self.y + self.HEIGHT < block.y + block.Blocks_Height))):
                self.xvel_to_right = 0
                self.xvel_to_left = MOVE_SPEED
                return [int(self.xvel_to_left), int(self.xvel_to_right)]
            # elif self.x + self.WIDTH < block.x:
            #     #if self.xvel < 0:                      # если движется влево
            #     self.xvel = 0
            #     return int(self.xvel)
            else:
                self.xvel_to_right = MOVE_SPEED
                self.xvel_to_left = MOVE_SPEED
                return [int(self.xvel_to_left), int(self.xvel_to_right)]

                # if self.yvel > 0:                      # если падает вниз
                #     self.rect.bottom = p.rect.top  # то не падает вниз
                #     self.onGround = True          # и становится на что-то твердое
                #     self.yvel = 0                 # и энергия падения пропадает
                #
                # if self.yvel < 0:                      # если движется вверх
                #     self.rect.top = p.rect.bottom  # то не движется вверх
                #     self.yvel = 0                 # и энергия прыжка пропадает

    def motion(self, blocks):
        global animCount
        global picture

        if animCount + 1 >= 30:
            animCount = 0
        keys = pygame.key.get_pressed()
        self.xvel_to_left = self.collide(blocks)[0]
        self.xvel_to_right = self.collide(blocks)[1]
        if keys[pygame.K_LEFT] and self.x > 5:
            animCount += 1
            self.image = self.walkRight[animCount // 5]
            self.x -= self.xvel_to_left
            self.lastMove = 'left'

        elif (keys[pygame.K_RIGHT] and self.x < 450):
            animCount += 1
            self.image = self.walkLeft[animCount // 5]
            self.x += self.xvel_to_right
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


    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

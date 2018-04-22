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
JUMP_SPEED = 20
lastMove = None
onGround = False
jumpCount = 10


class player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = MOVE_SPEED
        self.yvel = MOVE_SPEED
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = y
        self.xp = x
        self.yp = y
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
            if (self.x > block.x and self.x < block.x + block.Blocks_Width
                    and self.y + self.HEIGHT + self.yvel > block.y):
                if self.yp + self.HEIGHT < block.y or self.y == self.yp:
                    self.y = block.y - self.HEIGHT
                    self.yvel = 0
                    self.onGround = True
                else:
                    self.xvel = 0
                    self.x = block.x + block.Blocks_Width
                    self.onGround = True
                # return [int(self.xvel_to_left), int(self.xvel_to_right)]  # то не движется вправо
            elif ((self.x + self.WIDTH > block.x)
                  and (self.x + self.WIDTH < block.x + block.Blocks_Width)
                    and (self.y + self.HEIGHT + self.yvel > block.y)):
                if self.yp + self.HEIGHT < block.y or self.y == self.yp:
                    self.y = block.y - self.HEIGHT
                    self.yvel = 0
                    self.onGround = True
                else:
                    self.xvel = 0
                    self.x = block.x - self.WIDTH
                    self.onGround = True
                # return [int(self.xvel_to_left), int(self.xvel_to_right)]

            # elif self.x + self.WIDTH < block.x:
            #     #if self.xvel < 0:                      # если движется влево
            #     self.xvel = 0
            #     return int(self.xvel)
            # else:
                # self.xvel_to_right = MOVE_SPEED
                # self.xvel_to_left = MOVE_SPEED
                # return [int(self.xvel_to_left), int(self.xvel_to_right)]

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
        if keys[pygame.K_LEFT] and self.x > 5:
            self.xvel -= MOVE_SPEED
            self.xvel = max(self.xvel, -1 * MOVE_SPEED)
            self.lastMove = 'left'

        elif (keys[pygame.K_RIGHT] and self.x < 450):
            self.xvel += MOVE_SPEED
            self.xvel = min(self.xvel, MOVE_SPEED)
            self.lastMove = 'right'

        if self.onGround and (keys[pygame.K_UP] or keys[pygame.K_SPACE]):
            self.yvel = -1 * JUMP_SPEED
            self.onGround = False

        self.onGround = False
        if not self.onGround:
            self.yvel += 2
        self.collide(blocks)

        if self.xvel < -1 * MOVE_SPEED / 2:
            animCount += 1
            self.image = self.walkRight[animCount // 5]
        elif self.xvel > MOVE_SPEED / 2:
            animCount += 1
            self.image = self.walkLeft[animCount // 5]
        else:
            self.image = self.stay_picture
        self.xp = self.x
        self.x += self.xvel
        self.xvel *= 0.95
        self.yp = self.y
        self.y += self.yvel
        # if self.y > 400:
        #     self.y = 400
        #     self.yvel = 0
        #     self.onGround = True

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (int(self.x), int(self.y)), 1)
        pygame.draw.circle(win, (255, 0, 0), (int(
            self.x + self.WIDTH), int(self.y + self.HEIGHT)), 1)

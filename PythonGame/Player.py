import pygame
from Load_pictures import walkLeft
from Load_pictures import walkRight
from Load_pictures import stay_picture

picture = None
animCount = 0
WIDTH = 60
HEIGHT = 71
MOVE_SPEED = 5
JUMP_SPEED = 30
lastMove = None
onGround = False


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
        self.image = stay_picture
        self.rect = self.image.get_rect()
        self.onGround = onGround

    def camera_motion(self):
        pass

    def collide(self, blocks):
        for block in blocks:
            # Коллизия с блоком слева
            if (self.x > block.x and
                self.x < block.x + block.Blocks_Width - 2
                    and self.y + self.HEIGHT + self.yvel > block.y
                    and (self.y + self.HEIGHT > block.y
                         and self.y < block.y + block.Blocks_Height)
                    and self.yp < block.y + block.Blocks_Height):
                if not self.onGround:
                    self.xvel = 0
                    self.x = block.x + block.Blocks_Width

            # Коллизия с блоком справа
            elif ((self.x + self.WIDTH > block.x)
                  and (self.x + self.WIDTH < block.x + block.Blocks_Width and
                       self.y + self.HEIGHT > block.y)
                    and (self.y + self.HEIGHT + self.yvel > block.y)
                    and (self.y + self.HEIGHT > block.y
                         and self.y < block.y + block.Blocks_Height)
                  and self.yp < block.y + block.Blocks_Height):
                if not self.onGround:
                    self.xvel = 0
                    self.x = block.x - self.WIDTH

        for block in blocks:
            # Коллизия с блоком при движении вниз
            if (self.x > block.x and
                self.x < block.x + block.Blocks_Width - 2
                    and self.y + self.HEIGHT + self.yvel > block.y
                    and self.y < block.y + block.Blocks_Height):
                if self.yp > block.y + block.Blocks_Height:
                    self.y = block.y + block.Blocks_Height
                    self.yvel = 0
                elif (self.yp + self.HEIGHT < block.y or self.y == self.yp):
                    self.y = block.y - self.HEIGHT
                    self.yvel = 0
                    self.onGround = True

            # Коллизия с блоком при движении вверх
            elif ((self.x + self.WIDTH > block.x)
                  and (self.x + self.WIDTH < block.x + block.Blocks_Width)
                    and (self.y + self.HEIGHT + self.yvel > block.y)
                  and self.y < block.y + block.Blocks_Height):
                if self.yp > block.y + block.Blocks_Height:
                    self.y = block.y + block.Blocks_Height
                    self.yvel = 0
                elif (self.yp + self.HEIGHT < block.y or self.y == self.yp):
                    self.y = block.y - self.HEIGHT
                    self.yvel = 0
                    self.onGround = True

    def motion(self, blocks):
        global animCount
        global picture
        if animCount + 1 >= 30:
            animCount = 0
        keys = pygame.key.get_pressed()
        # Движение влево
        if keys[pygame.K_LEFT] and self.x > 5:
            self.xvel -= MOVE_SPEED
            self.xvel = max(self.xvel, -1 * MOVE_SPEED)
            self.lastMove = 'left'

        # Движение вправо
        elif (keys[pygame.K_RIGHT] and self.x < 450):
            self.xvel += MOVE_SPEED
            self.xvel = min(self.xvel, MOVE_SPEED)
            self.lastMove = 'right'

        # Прыжок(возможно, если стоим на земле)
        if self.onGround and (keys[pygame.K_UP] or keys[pygame.K_SPACE]):
            self.yvel = -1 * JUMP_SPEED
            self.onGround = False

        self.onGround = False
        # Свободное падение
        if not self.onGround:
            self.yvel += 2

        self.collide(blocks)
    # Смена анимации
        if self.xvel < -1 * MOVE_SPEED / 2:
            animCount += 1
            self.image = self.walkRight[animCount // 5]
        elif self.xvel > MOVE_SPEED / 2:
            animCount += 1
            self.image = self.walkLeft[animCount // 5]
        else:
            self.image = self.stay_picture
    # Записываем предыдущую координату.
        self.xp = self.x
        self.x += self.xvel
    # Делаем инерцию движения
        self.xvel *= 0.8
    # Записываем предыдущую координату.
        self.yp = self.y
        self.y += self.yvel

    def draw(self, win):
        pygame.draw.line(win, (0, 0, 0), (self.x - 200, 0),
                         (self.x - 200, 500))
        pygame.draw.line(win, (0, 0, 0), (self.x + 200, 0),
                         (self.x + 200, 500))
        pygame.draw.circle(win, (255, 0, 0), (int(self.x), int(self.y)), 1)
        pygame.draw.circle(win, (255, 0, 0), (int(
            self.x + self.WIDTH), int(self.y + self.HEIGHT)), 1)
        if self.onGround:
            pygame.draw.circle(win, (0, 0, 0), (int(
                self.x + self.WIDTH / 2), int(self.y)), 5)

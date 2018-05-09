import pygame
from Load_pictures import stay_picture
from Shell import shell
from time import time


onGround = False
WIDTH = 60
HEIGHT = 71
JUMP_SPEED = 30
Go_right = True
Go_left = False
start_time = time()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.x = x
        self.y = y
        self.xp = x
        self.yp = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.image = stay_picture
        self.rect = self.image.get_rect()
        self._x_speed = 2
        self._central_position = x
        self.onGround = onGround
        self.Go_right = Go_right
        self.Go_left = Go_left
        self.fires = pygame.sprite.Group()
        self.hp = 10
        self.isLive = True

    def collide(self, blocks):
        if self.isLive:
            for block in blocks:
                # Коллизия с блоком слева
                if (self.x > block.x + 2 and
                    self.x < block.x + block.Blocks_Width - 2
                        and self.y + self.HEIGHT + self.yvel > block.y
                        and (self.y + self.HEIGHT > block.y
                             and self.y < block.y + block.Blocks_Height)
                        and self.yp < block.y + block.Blocks_Height):
                    if not self.onGround:
                        self.xvel = 0
                        self.x = block.x + block.Blocks_Width
                    self.Go_right = True
                    self.Go_left = False
                # Колизия с блоком справа
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
                    self.Go_right = not True
                    self.Go_left = not False
            for block in blocks:
                # Колизия с блоком при движении вниз
                if (self.x > block.x + 2 and
                    self.x < block.x + block.Blocks_Width - 2
                        and self.y + self.HEIGHT + self.yvel > block.y
                        and self.y < block.y + block.Blocks_Height):
                    if (self.yp + self.HEIGHT < block.y or self.y == self.yp):
                        self.y = block.y - self.HEIGHT
                        self.yvel = 0
                        self.onGround = True

                # Колизия с блоком при движении вверх
                elif ((self.x + self.WIDTH > block.x)
                      and (self.x + self.WIDTH < block.x + block.Blocks_Width)
                        and (self.y + self.HEIGHT + self.yvel > block.y)
                      and self.y < block.y + block.Blocks_Height):
                    if (self.yp + self.HEIGHT < block.y or self.y == self.yp):
                        self.y = block.y - self.HEIGHT
                        self.yvel = 0
                        self.onGround = True

    def motion(self, blocks):
        if self.isLive:
            keys = pygame.key.get_pressed()
            if self.Go_right:
                self.x += self._x_speed / 4
            if self.Go_left:
                self.x -= self._x_speed / 4
            if self.onGround and (keys[pygame.K_z]):
                self.yvel = -1 * JUMP_SPEED
                self.onGround = False
            if not self.onGround:
                self.yvel += 2
            self.onGround = False
            self.collide(blocks)
            self.y += self.yvel

    def Hit_player(self, player, Blocks, win, shells):
        if self.isLive:
            global start_time
            if (abs(self.x - player.x) < 300
                    and abs(self.y - player.y) < 35):
                if self.x < player.x:
                    self.Go_left = False
                    self.Go_right = True
                    facing = 2
                    current_time = time()
                    if current_time - start_time > 0.1:
                        if len(shells) < 50:
                            shells.append(shell(round(self.x + self.WIDTH / 2),
                                                round(
                                self.y + self.HEIGHT / 2),
                                5, (255, 255, 0), facing))
                        start_time = current_time
                else:
                    self.Go_left = True
                    self.Go_right = False
                    current_time = time()
                    facing = -2
                    if current_time - start_time > 0.1:
                        if len(shells) < 50:
                            shells.append(shell(round(self.x + self.WIDTH / 2),
                                                round(
                                self.y + self.HEIGHT / 2),
                                5, (255, 255, 0), facing))
                        start_time = current_time

    def death(self, shells, win):
        if self.isLive:
            for shel in shells:
                if (shel.x + shel.radius > self.x
                    and shel.x + shel.radius < self.x + self.WIDTH
                        and shel.y > self.y and shel.y < self.y + self.HEIGHT):
                    self.hp -= 5
                    shells.pop(shells.index(shel))
        if self.hp <= 0:
            # pygame.draw.line(win, (0, 0, 0), (self.x + 200, 0),
            #                  (self.x + 200, 500))
            self.isLive = False

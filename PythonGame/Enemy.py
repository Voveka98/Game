import pygame
from Load_pictures import stay_picture
from Shell import shell
import random


onGround = False
WIDTH = 60
HEIGHT = 71
JUMP_SPEED = 30
Go_right = True
Go_left = False


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

    def collide(self, blocks):
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
        keys = pygame.key.get_pressed()
        if self.Go_right:
            self.x += self._x_speed / 4
        if self.Go_left:
            self.x -= self._x_speed / 4
        # if self.x < self._central_position + 25 and self.Go_right:
        #     self.x += self._x_speed
        # self.Go_right = False
        # self.Go_left = True
        # if self.x > self._central_position - 25 and self.Go_left:
        #     self.x -= self._x_speed / 2
        # self.Go_left = False
        # self.Go_right = True
        # if random.randint(1, 100) > 99 and self.onGround:
        if self.onGround and (keys[pygame.K_z]):
            self.yvel = -1 * JUMP_SPEED
            self.onGround = False
        if not self.onGround:
            self.yvel += 2
        self.onGround = False
        self.collide(blocks)
        self.y += self.yvel

    # def Hit_player(self, player, Blocks, win, entities):
    #     fires = []
    #     if (abs(self.x - player.x) < 100
    #             and abs(self.y - player.y) < 35):
    #         if self.x < player.x:
    #             self.Go_left = False
    #             self.Go_right = False
    #             shells = shell(round(self.x + self.WIDTH / 2),
    #                            round(self.y + self.HEIGHT / 2),
    #                            5, (255, 255, 0), facing=1)
    #             fires.append(shells)
    #             entities.add(shells)
    #         else:
    #             self.Go_left = True
    #             self.Go_right = False
    #             shells = shell(round(self.x + self.WIDTH / 2),
    #                            round(self.y + self.HEIGHT / 2),
    #                            5, (255, 255, 0), facing=-1)
    #             fires.append(shells)
    #             entities.add(shells)
    #         # self.motion(Blocks)
    #     for shells in fires:
    #         shells.draw(win)
    #         shells.motion(Blocks)

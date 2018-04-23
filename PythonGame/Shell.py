import pygame
from time import sleep
# from Player import lastMove
# from Player import WIDTH, HEIGHT
# from Player import player
# from random import randint


class shell(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, facing):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        # if lastMove == 'right':
        #     self.facing = 1
        # else:
        #     self.facing = -1
        self.facing = facing
        self.vel = 2 * self.facing
        self.image = pygame.Surface([self.radius, self.radius])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def del_shell(self):
        self.radius = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        # sleep(0.05)

    def motion(self, blocks):
        self.x += self.vel
        for block in blocks:
            if self.x > block.x and self.x < block.x + block.Blocks_Width and self.y > block.y and self.y < block.y + block.Blocks_Height:
                self.del_shell()

            # def appear(self):
            #     keys = pygame.key.get_pressed()
            #     shells = []
            #     if lastMove == 'right':
            #         facing = 1
            #     else:
            #         facing = -1
            #     if keys[pygame.K_f]:
            #         shells.append(shell(round(player.x + WIDTH/2)
            #                             , round(player.y + HEIGHT/2)
            #                             , 5, (randint(1, 255)
            #                                   , randint(1, 255)
            #                                   , randint(1, 255))
            #                             , facing))
            #     for bullet in shells:
            #         if bullet.x < 500 and bullet.x > 0:
            #             bullet.x += bullet.vel
            #         else:
            #             shells.pop(shells.index(bullet))
            #     return shells

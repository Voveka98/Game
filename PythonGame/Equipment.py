from Load_pictures import gun1_right_picture, gun1_left_picture
from Load_pictures import deal_with_it_picture, None_picture
import pygame


class equipment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = None_picture
        self.rect = self.image.get_rect()
        self.isLive = True

    def draw_gun(self, player):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.image = gun1_left_picture
            self.x = player.x - player.WIDTH / 2 + 9
            self.y = player.y + player.HEIGHT / 2
        elif keys[pygame.K_RIGHT]:
            self.image = gun1_right_picture
            self.x = player.x + player.WIDTH / 2 - 9
            self.y = player.y + player.HEIGHT / 2
        else:
            self.image = None_picture
            self.x = player.x + 6
            self.y = player.y + 13

    def draw_glass(self, player):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.image = None_picture
            self.x = player.x - player.WIDTH / 2 + 9
            self.y = player.y + player.HEIGHT / 2
        elif keys[pygame.K_RIGHT]:
            self.image = None_picture
            self.x = player.x + player.WIDTH / 2 - 9
            self.y = player.y + player.HEIGHT / 2
        else:
            self.image = deal_with_it_picture
            self.x = player.x + 6
            self.y = player.y + 12

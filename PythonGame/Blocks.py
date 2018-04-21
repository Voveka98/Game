import pygame


Blocks_Width = 20
Blocks_Height = 25
Blocs_Color = (50, 50, 50)


class Blocks(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.image = pygame.Surface([Blocks_Width, Blocks_Height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(x, y, Blocks_Width, Blocks_Height)

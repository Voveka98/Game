import pygame


Blocks_Width = 70
Blocks_Height = 70
Blocs_Color = (50, 50, 50)


class Blocks(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.Blocks_Width = Blocks_Width
        self.Blocks_Height = Blocks_Height
        self.image = pygame.Surface([self.Blocks_Width, self.Blocks_Height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

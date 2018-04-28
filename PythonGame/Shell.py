import pygame


class shell(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, facing):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 2 * self.facing
        self.image = pygame.Surface([self.radius, self.radius])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def del_shell(self):
        self.radius = 0

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, (int(self.x), int(self.y)), self.radius)

    def motion(self, blocks):
        self.x += self.vel
        for block in blocks:
            if (self.x > block.x and self.x < block.x + block.Blocks_Width and
                    self.y > block.y and
                    self.y < block.y + block.Blocks_Height):
                self.del_shell()

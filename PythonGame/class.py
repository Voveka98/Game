import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Python game")
bg = pygame.image.load('/home/vovek/PythonGame/assets/fon.jpg')
run = True
speed = 5
animCount = 0
picture = None
enemy_picture = pygame.image.load('/home/vovek/PythonGame/assets/boar.jpg')
walkLeft = [pygame.image.load('/home/vovek/PythonGame/assets/right1.jpg')
            , pygame.image.load('/home/vovek/PythonGame/assets/right2.jpg')
            , pygame.image.load('/home/vovek/PythonGame/assets/right3.jpg')
            , pygame.image.load('/home/vovek/PythonGame/assets/right4.jpg')
            , pygame.image.load('/home/vovek/PythonGame/assets/right5.jpg')
            , pygame.image.load('/home/vovek/PythonGame/assets/right6.jpg')
            ]
walkRight = [pygame.image.load('/home/vovek/PythonGame/assets/left1.jpg')
             , pygame.image.load('/home/vovek/PythonGame/assets/left2.jpg')
             , pygame.image.load('/home/vovek/PythonGame/assets/left3.jpg')
             , pygame.image.load('/home/vovek/PythonGame/assets/left4.jpg')
             , pygame.image.load('/home/vovek/PythonGame/assets/left5.jpg')
             , pygame.image.load('/home/vovek/PythonGame/assets/left6.jpg')
             ]

clock = pygame.time.Clock()


class player():
    def __init__(self, x, y, picture, walkLeft, walkRight):
        self.x = x
        self.y = y
        self.picture = picture
        self.walkRight = walkRight
        self.walkLeft = walkLeft

    def motion(self):
        global animCount
        global picture
        if animCount + 1 >= 30:
            animCount = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x > 5:
            animCount += 1
            picture = self.walkRight[animCount // 5]
            self.x -= 1
        elif (keys[pygame.K_RIGHT] and player.x < 450):
            animCount += 1
            picture = self.walkLeft[animCount // 5]
            self.x += 1
        else:
            picture = pygame.image.load('/home/vovek/PythonGame/assets/trump.jpg')

    def draw(self, win):
        win.blit(picture, (self.x, self.y))

    def collision(self, obj):
        if (self.x < obj.x and self.x + 60 > obj.x and self.y < obj.y
                and self.y + 71 > obj.y):
                pass


class crip():
    def __init__(self, x, y, picture):
        self.x = x
        self.y = y
        self.picture = picture

    def draw(self, win):
        win.blit(self.picture, (self.x, self.y))


enemy = crip(200, 435, enemy_picture)
player = player(15, 425, picture, walkLeft, walkRight)


# def main():
#     for e


def drawWindow():
    win.blit(bg, (0, 0))
    player.draw(win)
    enemy.draw(win)
    pygame.display.update()


while run:
    clock.tick(90)
    player.motion()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drawWindow()
pygame.quit()

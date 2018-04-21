import Blocks
import Player
import pygame
import Shell
from time import time


player = Player.player(50, 425)


Win_Width = 500
Win_Height = 500

pygame.init()
keys = pygame.key.get_pressed()
win = pygame.display.set_mode((Win_Width, Win_Height))
pygame.display.set_caption("Python game")
start_time = time()


shells = []
entities = pygame.sprite.Group()
blocks = []
entities.add(player)
level = [
       "-------------------------",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-                       -",
       "-        -              -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-                       -",
       "-------------------------"]

bg = pygame.image.load('/home/vovek/PythonGame/assets/fon.jpg')
clock = pygame.time.Clock()

x = y = 0
for row in level:
    for col in row:
        if col == '-':
            pf = Blocks.Blocks((50, 50, 50), x, y)
            entities.add(pf)
            blocks.append(pf)
            # pf = pygame.Surface((Blocks.Blocks_Width, Blocks.Blocks_Height))
            # pf.fill(Blocks.Blocs_Color)
            # win.blit(pf, (x, y))
        x += Blocks.Blocks_Width
    y += Blocks.Blocks_Height
    x = 0


def play_music():
    pygame.mixer.music.load('/home/vovek/PythonGame/music/Led')
    pygame.mixer.music.set_volume(0.45)
    pygame.mixer.music.play(-1, 0.0)


def drawWindow():

    win.blit(bg, (0, 0))

    for shell in shells:
        if shell.x < 500 and shell.x > 0:
            shell.x += shell.vel
        else:
            shells.pop(shells.index(shell))
    keys = pygame.key.get_pressed()
    global start_time
    if keys[pygame.K_f]:
        if player.lastMove == 'right':
            facing = 1
        else:
            facing = -1
        current_time = time()
        if current_time - start_time > 0.1:
            if len(shells) < 50:
                shells.append(Shell.shell(round(player.x + Player.WIDTH/2),
                                          round(player.y + Player.HEIGHT/2),
                                          5, (255, 000, 100), facing))
                start_time = current_time
    for e in entities:
        win.blit(e.image, (e.x, e.y))
    player.motion()
    player.collide(player.xvel, player.yvel, blocks)
    for shell in shells:

        shell.draw(win)
        shell.motion()
    # entities.draw(win)
    player.draw(win)
    pygame.display.update()


def main():
    play_music()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # entities.draw(win)
        # player.motion()
        drawWindow()


if __name__ == '__main__':
    main()

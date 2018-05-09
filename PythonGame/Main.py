import Blocks
import Player
import pygame
import Shell
from random import randint
from time import time
import Enemy


dx = 0

player = Player.player(150, 25)
enemies = pygame.sprite.Group()
enemy1 = Enemy.Enemy(350, 50)
enemy2 = Enemy.Enemy(100, 200)
enemies.add(enemy1)
enemies.add(enemy2)
bot_start_time = time()

Win_Width = 500
Win_Height = 1000

pygame.init()
keys = pygame.key.get_pressed()
win = pygame.display.set_mode((Win_Width, Win_Height))
pygame.display.set_caption("Python game")
start_time = time()


shells_from_player = []
shells_from_enemy = []
entities = pygame.sprite.Group()
blocks = []
entities.add(player)
entities.add(enemy1)
entities.add(enemy2)
level = [
    "-                                     -",
    "-                                     -",
    "-                                     -",
    "-                                     -",
    "-                                     -",
    "-                                     -",
    "-                                     -",
    "-              --                     -",
    "-   -                                 -",
    "-      ------                         -",
    "-                       -             -",
    "-- -                  ---    ---      -",
    "-     -       -----------          -- -",
    "---------------------------------------"]

# bg = pygame.image.load('/home/vovek/PythonGame/assets/fon.jpg')
clock = pygame.time.Clock()

x = y = 0
for row in level:
    for col in row:
        if col == '-':
            block = Blocks.Blocks((50, 50, 50), x, y)
            entities.add(block)
            blocks.append(block)
        x += Blocks.Blocks_Width
    y += Blocks.Blocks_Height
    x = 0


def create_enemy():
    enemy = Enemy.Enemy(player.x + 250, player.y)
    entities.add(enemy)
    enemies.add(enemy)


def play_music():
    pygame.mixer.music.load('/home/vovek/PythonGame/music/Led')
    pygame.mixer.music.set_volume(0)
    pygame.mixer.music.play(-1, 0.0)


def drawWindow():
    win.fill((200, 200, 200, 200))
    global start_time
    keys = pygame.key.get_pressed()
    if keys[pygame.K_y]:
        create_enemy()
    if keys[pygame.K_f]:
        if player.lastMove == 'right':
            facing = 1
        else:
            facing = -1
        current_time = time()
        if current_time - start_time > 0.1:
            if len(shells_from_player) < 50:
                shells_from_player.append(Shell.shell(round(player.x +
                                                            Player.WIDTH / 2),
                                                      round(
                                                          player.y +
                    Player.HEIGHT / 2),
                    5, (255, 000, 100),
                    facing))
                start_time = current_time
    for shell in shells_from_player:
        if abs(shell.x - player.x) < 1000:
            shell.x += shell.vel
        else:
            shells_from_player.pop(shells_from_player.index(shell))
    for shell in shells_from_enemy:
        if shell.x < 500 and shell.x > 0:
            shell.x += shell.vel
        else:
            shells_from_enemy.pop(shells_from_enemy.index(shell))
    for block in blocks:
        block.shell_collision(shells_from_enemy)
        block.shell_collision(shells_from_player)
    for enemy in enemies:
        enemy.motion(blocks)
        enemy.motion(blocks)
        enemy.death(shells_from_player, win)
        enemy.Hit_player(player, blocks, win, shells_from_enemy)
    player.motion(blocks, enemies)
    player.death(shells_from_enemy, win)
    for e in entities:
        if not e.isLive:
            entities.remove(e)
        win.blit(e.image, (e.x, e.y))
    shells = shells_from_player + shells_from_enemy
    for shell in shells:
        shell.draw(win)
        shell.motion(blocks)
    pygame.display.update()


def main():
    play_music()
    # run = True
    while player.player_run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.player_run = False
        drawWindow()


if __name__ == '__main__':
    main()

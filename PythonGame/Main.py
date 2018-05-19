import Blocks
import pygame
import Shell
from random import randint, choice
from time import time
import Enemy
from Constants import player, gun, glass, enemies, entities, shells_from_enemy
from Constants import shells_from_player, blocks, sf, win, level, Total_Width
from Constants import Total_Height, score, start_time, colors, True_coordinate


clock = pygame.time.Clock()
Current_Width = 0
x = 1
y = 0
for row in level:
    for col in row:
        if col == '-':
            block = Blocks.Blocks(choice(colors), x, y)
            entities.add(block)
            blocks.append(block)
            Current_Width += Blocks.Blocks_Width
            # print(block.x, block.y)
        x += Blocks.Blocks_Width
        Total_Height += Blocks.Blocks_Height
    Total_Width = Current_Width
    Current_Width = 0
    # print('================================')
    y += Blocks.Blocks_Height
    x = 0


def draw_score(win):
    global score
    font = pygame.font.Font(None, 30)
    text = font.render(
        "You've killed {} clones".format(score), True, (150, 0, 0))
    win.blit(text, [0, 50])


def create_enemy(position):
    global start_time
    if int(Total_Width - 830 - position) > 300:
        x = randint(int(200), int(Total_Width - 830 - position))
        enemy = Enemy.Enemy(x, 200)
        print(x)
        print('=-=-=-=-=-=-=-=')
    else:
        x = -1 * randint(int(100), int(830 + position))
        enemy = Enemy.Enemy(x, 200)
        print('spawn at', x, position)
        print('=-=-=-=-=-=-=-=')
    entities.add(enemy)
    enemies.add(enemy)
    print(enemy.x, enemy.y)


def play_music():
    pygame.mixer.music.load('/home/vovek/PythonGame/music/Led')
    pygame.mixer.music.set_volume(0.0)
    pygame.mixer.music.play(-1, 0.0)


def fire_shells():
    global start_time
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if player.lastMove == 'right':
            facing = 1
        else:
            facing = -1
        current_time = time()
        if current_time - start_time > 0.15:
            if len(shells_from_player) < 50:
                if keys[pygame.K_RIGHT]:
                    shells_from_player.append(Shell.shell(round(gun.x +
                                                                52),
                                                          round(
                                                              gun.y),
                                                          5, choice(colors),
                                                          facing * 1.5))
                elif keys[pygame.K_LEFT]:
                    shells_from_player.append(Shell.shell(round(player.x - 52 + player.WIDTH / 2),
                                                          round(
                                                              gun.y),
                                                          5, choice(colors),
                                                          facing * 1.5))
                else:
                    shells_from_player.append(Shell.shell(round(player.x +
                                                                player.WIDTH / 2),
                                                          round(
                                                              player.y + player.HEIGHT / 2),
                                                          5, choice(colors),
                                                          facing))
                start_time = current_time


def drawWindow():
    global score
    sf.fill((250, 200, 200, 200))
    global start_time
    keys = pygame.key.get_pressed()
    fire_shells()
    for shell in shells_from_player:
        if abs(shell.x - player.x) < 1000:
            shell.x += shell.vel
        else:
            shells_from_player.pop(shells_from_player.index(shell))
    for shell in shells_from_enemy:
        if shell.x < 1100 and shell.x > 0:
            shell.x += shell.vel
        else:
            shells_from_enemy.pop(shells_from_enemy.index(shell))
    for block in blocks:
        block.shell_collision(shells_from_enemy)
        block.shell_collision(shells_from_player)
    for enemy in enemies:
        # enemy.motion(blocks, enemies)
        enemy.motion(blocks)
        enemy.death(shells_from_player, sf)
        enemy.Hit_player(player, blocks, sf, shells_from_enemy)
        # print('enemy coordinate is', enemy.x)
        # print('=======================')
        if not enemy.isLive:
            enemies.remove(enemy)
            # print('enemy removed')
            # print('=============')
    gun.draw_gun(player)
    # glass.draw_glass(player)
    player.motion(blocks, enemies)
    global True_coordinate
    True_coordinate -= player.dx
    # print(True_coordinate)
    # print(level[-1])
    # print(Total_Width)
    for element in level[-1]:
        if (player.x < level[-1].index(element) * 70 and
                player.x + player.WIDTH > level[-1].index(element) * 70):
            a = level[-1].index(element)
            print(level[-1].index(element))
            print(a)
    player.death(shells_from_enemy, sf)
    for e in entities:
        if not e.isLive:
            global score
            score += 1
            entities.remove(e)
        sf.blit(e.image, (e.x, e.y))
    shells = shells_from_player + shells_from_enemy
    for shell in shells:
        shell.draw(sf)
        shell.motion(blocks)
    draw_score(sf)
    player.draw_hp(sf)
    if score > 10:
        glass.draw_glass(player)
    if keys[pygame.K_y] or len(enemies) < 5:
        create_enemy(True_coordinate)
    win.blit(sf, (0, 0))
    pygame.display.update()
    # pygame.display.flip()


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

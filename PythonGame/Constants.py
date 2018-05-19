import Player
import pygame
from time import time
import Enemy
import Equipment

Win_Width = 1000  # Ширина экрана
Win_Height = 1000  # Высота экрана
dx = 0
colors = [(255, 132, 0), (255, 0, 0), (171, 12, 207), (255, 111, 0)]
player = Player.player(150, 25)  # Создаем игрока
enemies = pygame.sprite.Group()  # Группа противников
enemy1 = Enemy.Enemy(350, 50)  # Противник
enemy2 = Enemy.Enemy(100, 200)
sf = pygame.Surface((Win_Width, Win_Height))  # Полотно
enemies.add(enemy1)  # добавляем врагов в группу
enemies.add(enemy2)
bot_start_time = time()
# Создаем спрайт пушки игрушки
gun = Equipment.equipment(player.x + player.WIDTH / 2,
                          player.y + player.HEIGHT / 2)
# Создаем спрайтов очков
glass = Equipment.equipment(player.x + player.WIDTH / 2,
                            player.y + player.HEIGHT / 2)


global score
score = 0
pygame.init()
keys = pygame.key.get_pressed()
win = pygame.display.set_mode((Win_Width, Win_Height))
pygame.display.set_caption("Python game")
start_time = time()

True_coordinate = 0
Total_Width = 0
Total_Height = 0
shells_from_player = []
shells_from_enemy = []
entities = pygame.sprite.Group()
blocks = []
entities.add(player)
entities.add(enemy1)
entities.add(enemy2)
entities.add(gun)
entities.add(glass)
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

import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply

from pygame.locals import *
from random import *


def draw_score_bombs_lifes():
    #绘制全屏炸弹数量
    bomb_text = bomb_font.render("✖ %d" % bomb_num, True, WHITE)
    text_rect = bomb_text.get_rect()
    screen.blit(bomb_image, (10, height - 10 - bomb_rect.height))
    screen.blit(bomb_text, (20 + bomb_rect.width, height - 5 - text_rect.height))

    #绘制剩余生命数量
    if life_num:
        for i in range(life_num):
            screen.blit(life_image, \
                        (width - 10 - (i + 1) * life_rect.width, \
                         height - 10 - life_rect.height))

    #绘制得分
    score_text = score_font.render("Score:%s" % str(score), True, WHITE)
    screen.blit(score_text, (10, 5))

def draw_me():
    #绘制我方飞机
    screen.blit(me.image1, me.rect)
pygame.init()
pygame.mixer.init()

bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("2021雷霆出击 V1.0 ---王琴")

background = pygame.image.load("images/background.png").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#载入游戏背景音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(background, (0, 0))

        draw_score_bombs_lifes()
        draw_me()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
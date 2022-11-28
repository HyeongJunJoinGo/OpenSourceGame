import pygame
import sys
import random
from random import random
from random import shuffle
from pygame.locals import *

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('Game Name')
screen = pygame.display.set_mode((400, 600), 0, 32)

font = pygame.font.SysFont(None, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

num = 0
article_num_x = 0
article_num_y = 0
article_situation_X = 0
article_situation_Y = 0
game_num = 0

x_len = 800  # 배경 크기


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


click = False


def main_menu():
    global click
    global num
    global article_num_x, article_situation_X
    global article_num_y, article_situation_Y
    global game_num
    while True:
        background = pygame.image.load('img/BG40.png')

        # 배경 움직이게 하기 ---->
        screen.blit(background, (num - (x_len - 400), 0))  # (배경 크기 - 400)
        screen.blit(background, (num - (x_len * 2 - 400), 0))  # (배경 크기 * 2 - 400)
        num = (num + 1) % x_len  # 배경 크기
        # 배경 움직이게 하기 ---->

        if article_situation_X != 0:
            if article_situation_X == 1:
                article_num_x += 8  # 400의 약수
                if article_num_x % 400 == 0:
                    article_situation_X = 0
            else:
                article_num_x -= 8  # 400의 약수
                if article_num_x % 400 == 0:
                    article_situation_X = 0
        if article_situation_Y != 0:
            article_num_y += 5
            if article_num_y == 600:
                article_situation_Y = 0

        if article_num_y == 600 and article_situation_Y == 0:
            pygame.time.delay(1000)
            if game_num == -2:
                game_m2()
            if game_num == -1:
                game_m1()
            if game_num == 1:
                game_p1()
            if game_num == 2:
                game_p2()

        draw_text('Main menu', font, BLACK, screen, 20, 20 + article_num_y)

        mx, my = pygame.mouse.get_pos()

        button_left = pygame.Rect(20, 270 + article_num_y, 15, 60)  # 좌측 버튼 판정용
        button_right = pygame.Rect(365, 270 + article_num_y, 15, 60)  # 우측 버튼 판정용

        button_1 = pygame.Rect(100 + article_num_x, 100 + article_num_y, 200, 50)  # 메인 화면 맨 위 버튼
        button_2 = pygame.Rect(100 + article_num_x, 200 + article_num_y, 200, 50)  # 메인 화면 중간 버튼
        button_3 = pygame.Rect(100 + article_num_x, 300 + article_num_y, 200, 50)  # 메인 화면 맨 아래 버튼
        button_game_m1 = pygame.Rect(-300 + article_num_x, 100 + article_num_y, 200, 50)  # -1번 게임
        button_game_m2 = pygame.Rect(-700 + article_num_x, 100 + article_num_y, 200, 50)  # -2번 게임
        button_game_p1 = pygame.Rect(500 + article_num_x, 100 + article_num_y, 200, 50)  # 1번 게임
        button_game_p2 = pygame.Rect(900 + article_num_x, 100 + article_num_y, 200, 50)  # 2번 게임

        pygame.draw.rect(screen, (51, 153, 255), button_1)
        pygame.draw.rect(screen, (153, 255, 255), button_2)
        pygame.draw.rect(screen, (153, 255, 255), button_3)
        nBY = 30  # next_Button_Y
        nBX = 15  # next_Button_X
        nBsX = 20  # next_Button_startX
        pygame.draw.polygon(screen, BLACK, [[nBsX, 300 + article_num_y], [nBsX + nBX, 300 + nBY + article_num_y], [nBsX + nBX, 300 - nBY + article_num_y]])
        pygame.draw.polygon(screen, BLACK, [[400 - nBsX, 300 + article_num_y], [400 - nBsX - nBX, 300 + nBY + article_num_y], [400 - nBsX - nBX, 300 - nBY + article_num_y]])
        pygame.draw.rect(screen, (51, 153, 255), button_game_m1)
        pygame.draw.rect(screen, (51, 153, 255), button_game_m2)
        pygame.draw.rect(screen, (51, 153, 255), button_game_p1)
        pygame.draw.rect(screen, (51, 153, 255), button_game_p2)

        draw_text('Main', font, WHITE, screen, 130 + article_num_x, 115 + article_num_y)
        draw_text('Game -1', font, WHITE, screen, -270 + article_num_x, 115 + article_num_y)
        draw_text('Game -2', font, WHITE, screen, -670 + article_num_x, 115 + article_num_y)
        draw_text('Game 1', font, WHITE, screen, 530 + article_num_x, 115 + article_num_y)
        draw_text('Game 2', font, WHITE, screen, 930 + article_num_x, 115 + article_num_y)
        draw_text('Option', font, WHITE, screen, 130 + article_num_x, 215 + article_num_y)
        draw_text('Move', font, WHITE, screen, 130 + article_num_x, 315 + article_num_y)

        if button_1.collidepoint((mx, my)):
            if click:
                game_p2()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                num += 100
        if button_left.collidepoint((mx, my)):
            if click:
                if article_situation_X == 0:
                    article_situation_X = 1
        if button_right.collidepoint((mx, my)):
            if click:
                if article_situation_X == 0:
                    article_situation_X = -1
        if button_game_m1.collidepoint((mx, my)):
            if click:
                if article_situation_Y == 0:
                    article_situation_Y = 1
                    game_num = -1
        if button_game_m2.collidepoint((mx, my)):
            if click:
                if article_situation_Y == 0:
                    article_situation_Y = 1
                    game_num = -2
        if button_game_p1.collidepoint((mx, my)):
            if click:
                if article_situation_Y == 0:
                    article_situation_Y = 1
                    game_num = 1
        if button_game_p2.collidepoint((mx, my)):
            if click:
                if article_situation_Y == 0:
                    article_situation_Y = 1
                    game_num = 2

        # 특정 상황에서 화면 어둡게 하기 ---->
        t_surface = screen.convert_alpha()
        t_surface.fill((0, 0, 0, min(255, int(article_num_y / 2.2))))
        screen.blit(t_surface, (0, 0))
        # 특정 상황에서 화면 어둡게 하기 ---->

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(120)


def game_m2():
    running = True
    while running:
        global click
        global article_num_x, article_num_y
        article_num_x = 0
        article_num_y = 0

        background = pygame.image.load('img/BG40.png')
        screen.blit(background, (0, 0))

        Gamem2_Button1 = pygame.Rect(50, 100, 200, 50)  # 메인 화면 맨 위 버튼
        pygame.draw.rect(screen, (42, 255, 84), Gamem2_Button1)
        mx, my = pygame.mouse.get_pos()

        if Gamem2_Button1.collidepoint((mx, my)):
            if click:
                click = False
                main_menu()

        draw_text('Game -2', font, (102, 153, 255), screen, 20, 20)
        #  이벤트 루프 =========================

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game_m1():
    running = True
    while running:
        global click
        global article_num_x, article_num_y
        article_num_x = 0
        article_num_y = 0

        background = pygame.image.load('img/BG40.png')
        screen.blit(background, (0, 0))

        Gamem1_Button1 = pygame.Rect(50, 100, 200, 50)  # 메인 화면 맨 위 버튼
        pygame.draw.rect(screen, (42, 255, 84), Gamem1_Button1)
        mx, my = pygame.mouse.get_pos()

        if Gamem1_Button1.collidepoint((mx, my)):
            if click:
                click = False
                main_menu()

        draw_text('Game -1', font, (102, 153, 255), screen, 20, 20)
        #  이벤트 루프 =========================

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def convert_time(ticks):
    ms = ticks % 1000
    sec = ticks // 1000
    minutes = sec // 60

    return str(minutes).zfill(2) + ":" + str(sec).zfill(2) + ":" + str(ms).zfill(3)


def game_p1():
    global click
    global article_num_x, article_num_y
    global num
    article_num_x = 0
    article_num_y = 0
    running = False
    before_difficulty = True
    cnt = 0
    MaxCnt = 25
    numlist = list(range(1, 26))
    shuffle(numlist)
    while before_difficulty:
        background = pygame.image.load('img/BG40.png')

        # 배경 움직이게 하기 ---->
        screen.blit(background, (num - (x_len - 400), 0))  # (배경 크기 - 400)
        screen.blit(background, (num - (x_len * 2 - 400), 0))  # (배경 크기 * 2 - 400)
        num = (num + 1) % x_len  # 배경 크기
        # 배경 움직이게 하기 ---->

        # 배경에 색깔 추가 ---->
        t_surface = screen.convert_alpha()
        t_surface.fill((255, 204, 204, 127))
        screen.blit(t_surface, (0, 0))
        # 배경에 색깔 추가 ---->

        game_p1_home1 = pygame.Rect(280, 20, 100, 50)  # 메인 화면 가는 버튼
        pygame.draw.rect(screen, (102, 204, 255), game_p1_home1)
        draw_text('Main', font, WHITE, screen, 290, 30)

        game_p1_easy = pygame.Rect(100, 150, 200, 50)  # 난이도 1번
        pygame.draw.rect(screen, (51, 153, 255), game_p1_easy)

        draw_text('Easy (1 to 25)', font, WHITE, screen, 110, 160)

        game_p1_mid = pygame.Rect(100, 300, 200, 50)  # 난이도 1번
        pygame.draw.rect(screen, (51, 153, 255), game_p1_mid)

        draw_text('Medium (1 to 50)', font, WHITE, screen, 110, 310)

        game_p1_hard = pygame.Rect(100, 450, 200, 50)  # 난이도 1번
        pygame.draw.rect(screen, (51, 153, 255), game_p1_hard)

        draw_text('Hard (1 to 100)', font, WHITE, screen, 110, 460)

        mx, my = pygame.mouse.get_pos()

        if game_p1_home1.collidepoint((mx, my)):
            if click:
                click = False
                main_menu()
        if game_p1_easy.collidepoint((mx, my)):
            if click:
                click = False
                running = True
                before_difficulty = False
                start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴
        if game_p1_mid.collidepoint((mx, my)):
            if click:
                click = False
                MaxCnt = 50
                running = True
                before_difficulty = False
                start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴
        if game_p1_hard.collidepoint((mx, my)):
            if click:
                click = False
                MaxCnt = 100
                running = True
                before_difficulty = False
                start_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴

        draw_text('Game 1', font, BLACK, screen, 20, 20)
        #  이벤트 루프 =========================

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

    while running:
        background = pygame.image.load('img/BG40.png')

        # 배경 움직이게 하기 ---->
        screen.blit(background, (num - (x_len - 400), 0))  # (배경 크기 - 400)
        screen.blit(background, (num - (x_len * 2 - 400), 0))  # (배경 크기 * 2 - 400)
        num = (num + 1) % x_len  # 배경 크기
        # 배경 움직이게 하기 ---->

        # 배경에 색깔 추가 ---->
        t_surface = screen.convert_alpha()
        t_surface.fill((255, 204, 204, 127))
        screen.blit(t_surface, (0, 0))
        # 배경에 색깔 추가 ---->

        game_p1_home = pygame.Rect(280, 20, 100, 50)  # 메인 화면 가는 버튼
        pygame.draw.rect(screen, (102, 204, 255), game_p1_home)
        draw_text('Main', font, WHITE, screen, 290, 30)
        oneto25button = []
        box_size = 60
        box_start = 55
        for i in range(5):
            for j in range(5):
                oneto25button.append(pygame.Rect(box_start + j * box_size, 200 + i * box_size, box_size - 10, box_size - 10))
                pygame.draw.rect(screen, (0, 0, 0), oneto25button[i * 5 + j])
                if cnt == MaxCnt:
                    draw_text("X", font, WHITE, screen, box_start + 5 + j * box_size, 205 + i * box_size)
                elif numlist[i * 5 + j] > MaxCnt:
                    draw_text("X", font, WHITE, screen, box_start + 5 + j * box_size, 205 + i * box_size)
                elif cnt < numlist[i * 5 + j]:
                    draw_text(str(numlist[i * 5 + j]), font, WHITE, screen, box_start + 5 + j * box_size, 205 + i * box_size)
                elif cnt == numlist[i * 5 + j]:
                    if numlist[i * 5 + j] < MaxCnt:
                        numlist[i * 5 + j] += 25
                    if numlist[i * 5 + j] > MaxCnt:
                        draw_text("X", font, WHITE, screen, box_start + 5 + j * box_size, 205 + i * box_size)
                    elif cnt <= numlist[i * 5 + j]:
                        draw_text(str(numlist[i * 5 + j]), font, WHITE, screen, box_start + 5 + j * box_size, 205 + i * box_size)
        mx, my = pygame.mouse.get_pos()

        if game_p1_home.collidepoint((mx, my)):
            if click:
                click = False
                main_menu()

        draw_text('Game 1', font, BLACK, screen, 20, 20)
        draw_text(str(cnt), font, BLACK, screen, 40, 60)

        if cnt != MaxCnt:
            now_ticks = pygame.time.get_ticks()  # 현재 tick 을 받아옴
            now_time = convert_time(now_ticks - start_ticks)

        cell_text = font.render(now_time, True, WHITE) # text render
        screen.blit(cell_text, (150, 540))
        #  이벤트 루프 =========================

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        for k in range(25):
            if oneto25button[k].collidepoint((mx, my)):
                if click:
                    if numlist[k] == cnt + 1:
                        if cnt != MaxCnt:
                            cnt += 1


        pygame.display.update()
        mainClock.tick(60)


def game_p2():
    global click
    global article_num_x, article_num_y
    global num
    article_num_x = 0
    article_num_y = 0
    running = True
    l1 = list(range(1, 4))
    l2 = list(range(1, 4))
    num_list = l1 + l2
    shuffle(num_list)
    print(num_list)
    card_state = [0] * 6
    flip_ing = False
    fliping_card = 0
    back_flip = False
    flip_cnt = 0
    flip_card = 0
    while running:
        background = pygame.image.load('img/BG40.png')

        # 배경 움직이게 하기 ---->
        screen.blit(background, (num - (x_len - 400), 0))  # (배경 크기 - 400)
        screen.blit(background, (num - (x_len * 2 - 400), 0))  # (배경 크기 * 2 - 400)
        num = (num + 5) % x_len  # 배경 크기
        # 배경 움직이게 하기 ---->

        # 배경에 색깔 추가 ---->
        t_surface = screen.convert_alpha()
        t_surface.fill((255, 204, 204, 127))
        screen.blit(t_surface, (0, 0))
        # 배경에 색깔 추가 ---->

        game_p2_home = pygame.Rect(280, 20, 100, 50)  # 메인 화면 가는 버튼
        pygame.draw.rect(screen, (102, 204, 255), game_p2_home)
        draw_text('Main', font, WHITE, screen, 290, 30)

        card_back = pygame.image.load('img/Card_Back.jpg')
        card_back = pygame.transform.scale(card_back, (50, 70))
        card_back2 = pygame.image.load('img/Card_Back.jpg')
        card_back2 = pygame.transform.scale(card_back2, (50, 70))
        card = []
        card_button = []

        for i in range(2):
            for j in range(3):
                cardname = "img/card" + str(num_list[i * 3 + j]) + ".png"
                card.append(pygame.image.load(cardname))
                card[i * 3 + j] = pygame.transform.scale(card[i * 3 + j], (50, 70))
                card_button.append(pygame.Rect(100 + i * 70, 100 + j * 100, 50, 70))
                if card_state[i * 3 + j] == 0:
                    screen.blit(card_back, (100 + i * 70, 100 + j * 100))
                elif card_state[i * 3 + j] == 1:
                    if flip_ing and fliping_card == i * 3 + j:
                        card[i * 3 + j] = pygame.transform.scale(card[i * 3 + j], (max(0, flip_cnt * 10 - 50), 70))
                        card_back2 = pygame.transform.scale(card_back2, (max(0, 50 - flip_cnt * 10), 70))
                        screen.blit(card[i * 3 + j], (150 + i * 70 - flip_cnt * 5, 100 + j * 100))
                        screen.blit(card_back2, (100 + i * 70 + flip_cnt * 5, 100 + j * 100))
                        if flip_cnt < 10:
                            flip_cnt += 1
                        else:
                            flip_cnt = 0
                            flip_ing = False
                            flip_card = min(flip_card + 1, 2)
                    else:
                        card[i * 3 + j] = pygame.transform.scale(card[i * 3 + j], (50, 70))
                        screen.blit(card[i * 3 + j], (100 + i * 70, 100 + j * 100))
                else:
                    screen.blit(card[i * 3 + j], (100 + i * 70, 100 + j * 100))

        if flip_card == 2:
            a = []
            flip_card = 0
            for k in range(6):
                if card_state[k] == 1:
                    a.append(k)
                    print(a)
            pygame.time.delay(200)
            if num_list[a[0]] == num_list[a[1]]:
                card_state[a[0]] = 2
                card_state[a[1]] = 2
            else:
                card_state[a[0]] = 0
                card_state[a[1]] = 0


        mx, my = pygame.mouse.get_pos()

        if game_p2_home.collidepoint((mx, my)):
            if click:
                click = False
                main_menu()

        for i in range(2):
            for j in range(3):
                if card_button[i * 3 + j].collidepoint((mx, my)):
                    if click and not flip_ing:
                        if card_state[i * 3 + j] == 0:
                            click = False
                            flip_ing = True
                            fliping_card = i * 3 + j
                            card_state[i * 3 + j] = 1
                            flip_cnt = 1

        draw_text('Game 2', font, (102, 153, 255), screen, 20, 20)
        #  이벤트 루프 =========================

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    while running:
        background = pygame.image.load('img/BG40.png')
        screen.blit(background, (0, 0))

        draw_text('Options', font, (102, 153, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)


main_menu()

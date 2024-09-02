import pygame
import math
import random

# 1. 게임초기화
pygame.init()
# 2. 게임창옵션설정
size = [500, 700]
screen = pygame.display.set_mode(size)
title = 'HANGMAN'
pygame.display.set_caption(title)

# 3. 게임내필요한설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
hint_font = pygame.font.Font("C:/Windows/Fonts/ALGER.TTF", 80)
entry_font = pygame.font.Font("C:/Windows/Fonts/ALGER.TTF", 60)

# 1.
# A가영어단어를1개생각한다.
with open('voca.txt', encoding='UTF-8') as f:
    raw_data = f.read()
data_list = raw_data.split("\n")
data_list = data_list[:-1]

while True:
    r_index = random.randrange(0, len(data_list))

    word = data_list[r_index].replace(u'\xa0', u' ').split(" ")[1]
    
    if len(word) <= 6 : break
word = word.upper()
# 2.
# 단어의글자수만큼밑줄을긋는다.

word_show = "_" * len(word)

try_num = 0 # 게임 시도 횟수
ok_list = []
no_list = []


def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    
    return tuple(temp_list)

try_num = 0

drop = False
# 4. 메인이벤트
exit = False
k = 0

while not exit:
    # 4-1. FPS(Frame per second) 설정
    clock.tick(60) # 60fps 설정
    # 4-2. 각종입력감지
    for event in pygame.event.get(): # 키보드 입력을 리스트로 저장하고 반환함
        if event.type == pygame.QUIT:
            exit = True
    
    # 4-3. 입력, 시간에따른변화
    k += 1
    if enter_go == True:
        ans = entry_text
        result = word.find(ans) # 있으면 해당하는 위치의 첫 번째 인덱스 값을 반환함

        if result == -1 : # 없을 때
            print("WRONG")
            try_num += 1
            no_list.append(ans)
        else :
            print("RIGHT")
            ok_list.append(ans)
            for i in range(len(word)):
                if word[i] == ans:
                    word_show = word_show[:i] + ans + word_show[i+1:]
        enter_go = False
        entry_text = ""
    
    # 4-4. 그리기
    screen.fill(black)
    A = tup_r((0, size[1]*2/3))
    B = (size[0], A[1])
    C = tup_r((size[0] * 1/6 , A[1]))
    D = (C[0], C[0])
    E = tup_r((size[0] /2, D[1]))
    F = tup_r((E[0], E[1]+size[0]/6))
        
    pygame.draw.line(screen, white, A, B, 3)
    pygame.draw.line(screen, white, C, D, 3)
    pygame.draw.line(screen, white, D, E, 3)
    
    if drop == False:
        pygame.draw.line(screen, white, E, F, 3)
    # 얼굴
    r_head = round(size[0] / 12)
    if drop == True :     G = (F[0], F[1]+r_head+k*7)
    else :    G = (F[0], F[1]+r_head)
    pygame.draw.circle(screen, white, G, r_head, 3)
    
    # 목
    H = (G[0], G[1]+r_head)
    I = (H[0], H[1]+r_head)
    pygame.draw.line(screen, white, H, I, 3)
    
    #팔(각도는 라디안으로 변환해야함)
    l_arm = r_head * 2
    J = (I[0] - l_arm * math.cos(30*math.pi/180), I[1] + l_arm * math.sin(30*math.pi/180))
    K = (I[0] + l_arm * math.cos(30*math.pi/180), I[1] + l_arm * math.sin(30*math.pi/180))
    J = tup_r(J)
    K = tup_r(K)
    pygame.draw.line(screen, white, I, J, 3)
    pygame.draw.line(screen, white, I, K, 3)
    
    #몸
    L = (I[0], I[1] + l_arm)
    pygame.draw.line(screen, white, I, L, 3)
    
    #다리
    l_leg = round(l_arm * 1.5)
    M = (L[0] - l_arm * math.cos(60*math.pi/180), L[1] + l_arm * math.sin(60*math.pi/180))
    N = (L[0] + l_arm * math.cos(60*math.pi/180), L[1] + l_arm * math.sin(60*math.pi/180))
    M = tup_r(M)
    N = tup_r(N)
    pygame.draw.line(screen, white, L, M, 3)
    pygame.draw.line(screen, white, L, N, 3)

    
    if drop == False and try_num == 8:

        O = tup_r((size[0]/2 - size[0]/6, E[1]/2+F[1]/2))
        P = (O[0]+k*2, O[1])
        if P[0] > (size[0]/2 + size[0]/6):
            P = tup_r((size[0]/2 + size[0]/6, O[1]))
            drop = True
            k = 0
        pygame.draw.line(screen, red, O, P, 3)
        
    
    # 힌트 표시하기
    # word_show = "___"
    hint = hint_font.render(word_show, True, white)
    
    hint_size = hint.get_size()
    hint_pos = tup_r((size[0]/2 - hint_size[0]/2, size[1]*4/5 - hint_size[1]/2))
    screen.blit(hint, hint_pos)
    
    # 입력창 표시하기
    # 배경을 먼저 그리고, 뒤에 글자를 표시한다
    entry_text = "Q"
    entry = entry_font.render(entry_text, True, black)
    entry_size = entry.get_size()
    entry_pos = (size[0]/2-entry_size[0]/2, size[1]*17/18-entry_size[1]/2)
    
    entry_bg_size = 80
    pygame.draw.rect(screen, white, tup_r((size[0]/2-entry_bg_size/2, size[1]*17/18-entry_bg_size/2
                                     , entry_bg_size, entry_bg_size)))
    
    screen.blit(entry, entry_pos) # 글자 표시
    
    
    
    # 4-5. 업데이트
    pygame.display.flip()
 # 5. 게임종료
pygame.quit()    
import random

with open('voca.txt', encoding='UTF-8') as f:
    raw_data = f.read()
# print(raw_data)
# print(raw_data.split("\n")[-1])
data_list = raw_data.split("\n")
data_list = data_list[:-1]

while True:
    r_index = random.randrange(0, len(data_list))

    word = data_list[r_index].replace(u'\xa0', u' ').split(" ")[1]
    
    if len(word) <= 6 : break
# 1.
# A가영어단어를1개생각한다.
print(word)
# 2.
# 단어의글자수만큼밑줄을긋는다.

word_show = "_" * len(word)
print(word_show)

try_num = 0 # 게임 시도 횟수
ok_list = []
no_list = []

# 3.
# B가단어에포함될것같은알파벳을하나씩말한다.

while True:
    ans = input().upper()
    print(ans)

    # 4.
    # 알파벳이단어에포함되면밑줄에알파벳을채워놓고포함되지않는다면사람을1획씩그린다.

    result = word.find(ans) # 있으면 해당하는 위치의 첫 번째 인덱스 값을 반환함
    print(result)

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
        print(word_show)
# 사람이먼저완성되면출제자A가이긴다.단어가먼저완성되면단어를맞힌사람B가이긴다.
    if try_num == 7: break
    
    if word_show.find("_") == -1: break


print(word)
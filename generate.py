from random import *
import os
import io
print("Загрузите воросы из билетов в файл q.txt")
if input("1 - винда\n2 - линух\n") == "1":
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')
f = io.open("q.txt", encoding='utf-8').readlines()
quest = [x.replace('\n','')for x in f]
QUESTS = quest.copy()
quest.pop()
generated_list = []

number_of_questions = int(input("Воросов в твоем билете - "))
clear()
print(f"Тебя приветсвует ебучий тест на из {len(quest)} вопросов.")

while quest:
    for i in range(number_of_questions):
        if len(quest) != 0:
            q = choice(quest)
            print(f"{i+1}. {q} (номер вопроса {QUESTS.index(q) + 1})")
            quest.remove(q)
    print("шариш?")
    print("1 - да\n\"не 1\" - Заебался")
    a = input()
    if a == "1":
        clear()
        print("красава","Осталось вопросов:",len(quest))
    else:
        clear()
        print("Пока")
        quit()
print("Это пизда")




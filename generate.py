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
quest.pop()
generated_list = []
r = 0
w = 0
number_of_questions = int(input("Воросов в твоем билете - "))
print(f"Тебя приветсвует ебучий тест на {int(len(quest)/number_of_questions) + int(len(quest)%number_of_questions)} вопросов.")

while quest:
    for i in range(number_of_questions):
        if len(quest) != 0:
            q = choice(quest)
            print(f"{i+1}. {q}")
            quest.remove(q)
    print("шариш?")
    print("1 - да\n2 - нет, давай рерол\n3 - Заебался")
    a = input()
    if a == "1":
        clear()
        r +=1
        print("красава","Осталось билетов:",int(len(quest)/2))
    elif a == "2":
        clear()
        w+=1
        print("🤦","Осталось билетов:",int(len(quest)/2))
    else:
        clear()
        print("Пока")
        print(f"Знаешь - {r}\nНе знаешь - {w}")
        quit()
print("Это пизда")
print(f"Знаешь - {r}\nНе знаешь - {w}")




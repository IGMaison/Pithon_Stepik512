nsps = [["global", None]]
n = int(input())
for i in range(n):
    c1, c2, c3 = input().split()
    if c1 == "create":
        nsps.append([c2, c3])
    elif c1 == "add":
        for j in range(len(nsps)):
            if c2 == nsps[j][0]:
                nsps[j].append(c3)
                break
    elif c1 == "get":
        j, res = 0, None
        while j < len(nsps):
            if c2 == nsps[j][0] and c3 in nsps[j]:
                res = nsps[j][0]
                break
            elif c2 == nsps[j][0]:
                c2 = nsps[j][1]
                j = 0
            else:
                j += 1
        print(res)

'''Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку
 создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

    create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
    add <namespace> <var> – добавить в пространство <namespace> переменную <var>
    get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из 
    пространства <namespace>, или None, если такого пространства не существует'''

s, t = input(), input()
cnt = -1
pos = 0
while pos >= 0:
    pos = s.find(t, pos)
    if pos >= 0: pos += 1
    cnt += 1
print(cnt)

'''Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa'''

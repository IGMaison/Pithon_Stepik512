import sys, re

sys.stdout.writelines(filter(re.compile(r'\b(.+)\1\b').search, sys.stdin))

'''

Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

Sample Input:

blabla is a tandem repetition
123123 is good too
go go
aaa

Sample Output:

blabla is a tandem repetition
123123 is good too

'''

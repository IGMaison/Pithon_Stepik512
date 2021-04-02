import sys, re

for line in sys.stdin:
    line = line.strip()
    sys.stdout.writelines(re.sub('human', 'computer', line))


'''

Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

Sample Input:

I need to understand the human mind
humanity

Sample Output:

I need to understand the computer mind
computerity

Напишите прог'''
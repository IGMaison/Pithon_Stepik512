import sys, re

sys.stdout.writelines(filter(re.compile(r'\\').search, sys.stdin))

'''
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".

Sample Input:

\w denotes word character
No slashes here

Sample Output:

\w denotes word character

'''

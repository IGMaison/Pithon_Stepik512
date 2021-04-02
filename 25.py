import sys, re

for line in sys.stdin:
    if re.search(r'z.{3}z', line.rstrip()):
        print(line.rstrip())

'''
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz

Sample Output:

zabcz
zzxzz

'''

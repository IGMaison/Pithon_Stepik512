import sys, re


def f(x):
    x = x.group(0)
    return x[1] + x[0] + x[2:]


for line in sys.stdin:
    line = line.strip()
    print(re.sub(r'(\b\w{2,}\b)', f, line))

'''
import sys, re

for line in sys.stdin:
    line = line.strip()
    splitline = re.split(r'(\b\w{2,}\b)', line)
    for part in range(len(splitline)):
        check = re.fullmatch(r'(\b\w{2,}\b)', splitline[part])
        if check:
            splitline[part] = splitline[part][1] + splitline[part][0] + splitline[part][2:]
    print(''.join(splitline))
'''

'''
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.

Sample Input:

this is a text
"this' !is. ?n1ce,

Sample Output:

htis si a etxt
"htis' !si. ?1nce,

'''
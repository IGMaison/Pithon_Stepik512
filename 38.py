import requests, re, time

with open('dataset38.txt', 'r') as f:
    for checking_num in f:
        checking_num = re.search(r'\d*', checking_num.strip())
        if checking_num[0]:
            api_url = 'http://numbersapi.com/' + checking_num[0] + '/math?json'
            res = requests.get(api_url).json()
            print('Interesting' if res['found'] else 'Boring')
            time.sleep(1)


''' этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать,
 существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring'''

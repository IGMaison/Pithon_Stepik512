import csv

crimes2015 = {}
with open('crimes.csv', 'r') as crime_file:
    crimes = csv.reader(crime_file)
    for row in crimes:
        if '2015' in row[2]:
            new_val = crimes2015.setdefault(row[5], 0)
            crimes2015[row[5]] = new_val + 1
print(sorted(crimes2015.items(), key=lambda x: x[1], reverse=True)[0])

'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 
года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv'''

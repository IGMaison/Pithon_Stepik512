import json


def childs(the_class):
    count = set()
    for json_obj in json_list:
        if the_class in json_obj['parents']:
            count.add(json_obj['name'])
            count = count | childs(json_obj['name'])
    return count


class_set = set()
answer = {}
json_list = json.loads(input())
for json_obj in json_list:
    class_set.add(json_obj['name'])
    for parent in json_obj['parents']:
        class_set.add(parent)
for the_class in class_set:
    answer.setdefault(the_class, 1)
for the_class in class_set:
    answer[the_class] += len(childs(the_class))
for obj in sorted(answer.items()):
    print(obj[0], ':', obj[1])


'''

Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле 
name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass


Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от
 одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Sample Output:

A : 3
B : 1
C : 2

'''

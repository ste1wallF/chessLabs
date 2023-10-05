from work import *
while True:
    try:
        k = int(input('Введите  x1'))
        l = int(input('Введите  y1'))
        m = int(input('Введите  x2'))
        n = int(input('Введите  y2'))
        break
    except ValueError:
        print('Введите число от 1 до 8!')

k1 = Pole(k, l)                                                       # задание 1
k2 = Pole(m, n)

if (k1.x + k1.y) % 2 == (k2.x + k2.y) % 2:
    print(f'Клетки ({k1.x}:{k1.y}) и ({k2.x}:{k2.y}) одного цвета')
else:
    print(f'Клетки ({k1.x}:{k1.y}) и ({k2.x}:{k2.y}) разных цветов')



figura = str(input(f' Какая фигура стоит на поле ({k1.x}:{k1.y})? /'
                f'Ферзь/Ладья/Слон/Конь'))                              # задание 2

c2 = k2.cord
figura1 = ''
if figura== 'Ферзь':
    figura1 = Ferz(k, l)
if figura== 'Ладья':
    figura1 = Ladia(k, l)
if figura== 'Слон':
    figura1 = Slon(k, l)
if figura== 'Конь':
    figura1 = Kon(k, l)

kor_a = figura1.hod()                                              # создание списка клеток, на которые можно попасть за 1 ход

if c2 in kor_a:
    print(f'{figura1.name} угрожает полю {c2}')
else:
    print(f'{figura1.name} не угрожает полю {c2}')


figura= str(input(f' Какая фигура стоит на поле ({k1.x}:{k1.y})? /'
                f'Ферзь/Ладья/Слон/Конь '))                              # задание 3

c2 = k2.cord
figura1 = ''
figura2 = ''
if figura == 'Ферзь':
    figura1 = Ferz(k, l)
    figura2 = Ferz(m, n)
if figura == 'Ладья':
    figura1 = Ladia(k, l)
    figura2 = Ladia(m, n)
if figura == 'Слон':
    figura1 = Slon(k, l)
    figura2 = Slon(m, n)
if figura == 'Конь':
    figura1 = Kon(k, l)
    figura2 = Kon(m, n)

kor_a = figura1.hod()
Fk = []
if c2 in kor_a:
    print(f'{figura1.name} может за 1 ход попасть на поле  {c2}')
else:
    print(f'{figura1.name} не может за 1 ход попасть на поле {c2}')
    kor_a2 = figura2.hod()
    for i in kor_a:
        if i in kor_a2:
            Fk.append(i)
    if len(Fk) != 0:
        print(f'Может попасть за 2 хода через поле(поля) {Fk}')
    else:
        print(f'Не может за 2 хода попасть на поле {c2}')
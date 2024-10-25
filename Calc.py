import random

class Dvoich_calc():
    def Calc2():
        number = int(input('Введите число: '))
        binary = format(number, "b")
        print(number, '=', binary)
        print('Удачи','\n')
    def Calc8():
        number = int(input('Введите число: '))
        binary = format(number, "o")
        print(number, '=', binary)
        print('Удачи','\n')
    def Calc16():
        number = int(input('Введите число: '))
        binary = format(number, 'x')
        print(number, '=', binary)
        print('Удачи','\n')

class Calculator():    
    def clojenie():
        print('Вы выбрали сложение чисел')
        change1 = int(input('Введите первое число: '))
        change2 = int(input('Введите второе число: '))
        return print('Ваш ответ:', change1 + change2,'\n')
    def vichitanie():
        print('Вы выбрали сложение чисел')
        change1 = int(input('Введите первое число: '))
        change2 = int(input('Введите второе число: '))
        return print('Ваш ответ:', change1 - change2,'\n')
    def ymnogenie():
        print('Вы выбрали сложение чисел')
        change1 = int(input('Введите первое число: '))
        change2 = int(input('Введите второе число: '))
        return print('Ваш ответ:', change1 * change2,'\n')
    def delenie():
        print('Вы выбрали сложение чисел')
        change1 = int(input('Введите первое число: '))
        change2 = int(input('Введите второе число: '))
        return print('Ваш ответ:', change1 / change2,'\n')

class orel_reshka():
    def start():
        changing = ['Орел', 'Решка']
        result = random.choice(changing)
        return print('Выпал: ',result,'\n')





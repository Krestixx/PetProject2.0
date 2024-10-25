import Calc
while True:
    try:
        print('1: Калькулятор систем счисления')
        print('2: Калькулятор')
        print('3: Орел или Решка')
        print('0: Выход')
    
        user_change_menu = int(input('Выбор: '))
    
        if user_change_menu == 1:
            print('Вы выбрали калькулятор системы счисления!')
            print('Какую систему счисления будете зайдествовать?: ')
            print(' Из десятичной в двоичную: 1 \n Из десятичной в восьмиричную: 2 \n Из десятичной в шестнадцатиричную: 3 \n')
            change_dvoich_system = int(input('Выбор: '))
            if change_dvoich_system == 1:
                Calc.Dvoich_calc.Calc2()
            if change_dvoich_system == 2:
                Calc.Dvoich_calc.Calc8()
            if change_dvoich_system == 3:
                Calc.Dvoich_calc.Calc16()
        
        if user_change_menu == 2:
            print('Вы выбрали калькулятор!')
            print('Какое действие выбирете?')
            print(' Сложение: 1 \n Вычитание: 2 \n Умножение: 3 \n Деление: 4 \n')
            change_calculator_menu = int(input('Выбор: '))
            if change_calculator_menu == 1:
                Calc.Calculator.clojenie()
            elif change_calculator_menu == 2:
                Calc.Calculator.vichitanie()
            elif change_calculator_menu == 3:
                Calc.Calculator.ymnogenie()
            elif change_calculator_menu == 4:
                Calc.Calculator.delenie()

        if user_change_menu == 3:
            print()
            Calc.orel_reshka.start()
        
        if user_change_menu == 0:
            break
        else:
            print('== Такой выбор не предусмотрен ==')
    except ValueError:
        print('== Такой выбор не предусмотрен ==')
    
# Ваше решение

def Calculator(num1,num2,act):
    # %.2f - фоматированный вывод числа с запятой, 2 символа после запятой, а % -это позиция переменной в строке вывода
    if act == '+':
        return print('%.2f + %.2f = %.2f' % (num1, num2, num1+num2))
    elif act == '-':
        return print('%.2f - %.2f = %.2f' % (num1, num2, num1-num2))
    elif act == '*':
        return print('%.2f * %.2f = %.2f' % (num1, num2, num1*num2))
    elif act == '/':
        if num2 != 0:
            return print('%.2f / %.2f = %.2f' % (num1, num2, num1/num2))
        else:
            return print("Деление на ноль!")

act=''
while True:
    print("Выберите действие которое хотите сделать:\n"
          "Сложить: +\n"
          "Вычесть: -\n"
          "Умножить: *\n"
          "Поделить: /\n"
          "Выйти: q\n")
    act = input("Действие: ")
    if act == "q":
        print("Выход из программы")
        break
    if act in ('+', '-', '*', '/'):
        num1 = float(input("num1 = "))
        num2 = float(input("num2 = "))
        Calculator(num1, num2, act)
    else:
        print('Это не вычислимо, еще раз?')
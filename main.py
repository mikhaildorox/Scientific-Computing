# Scientific computing with python
from prettytable import PrettyTable
expressions = ['1 + 13', '10 + 2', '3 + 1000', '40000 + 200', '1500 - 10', '500 - 654']
operators = '-+'


def arithmetic_arranger(expressions, answer):  # Вычисление выражений
    myTab = PrettyTable()
    result = 0
    iteration = 1
    error = 0
    for expression in expressions:  # Выбирается по одному выражению из списка выражений
        columns = ['expression ' + str(iteration)]
        expr_split = (expression.split())  # разбиваю выражение
        first_number = expr_split[0] # первое число
        second_number = expr_split[2] # второе число
        operator = expr_split[1] # оператор
        if not first_number.isdigit() or not second_number.isdigit():
            print(f'expession {iteration}')
            print('Error: Numbers must only contain digits.')
            iteration += 1
            error += 1
            if error > 5:
                print('Error: Too many problems.')
                break
            continue
        if len(first_number) > 4 or len(second_number) > 4:
            print(f'expession {iteration}')
            print('Error: Numbers cannot be more than four digits.')
            iteration += 1
            error += 1
            if error > 5:
                print('Error: Too many problems.')
                break
            continue
        if operator not in operators:  # Нахожу + или -
            print(f'expession {iteration}')
            print("Error: Operator must be '+' or '-'.")
            iteration += 1
            error += 1
            if error > 5:
                print('Error: Too many problems.')
                break
            continue
        if '+' in expr_split:  # если в выражении плюс,
            result = int(first_number) + int(second_number)  # то складываю числа
        elif '-' in expr_split:  # если в выражении -,
            result = int(first_number) - int(second_number)  # то вычитаю

        qty_whitespace1, qty_whitespace2 = qty_whitespace(
            expression)  # нахожу количество пробелов для вывода на экран выражения в столбик
        qty_lines = 1 + qty_whitespace2 + len(second_number)
        qty_whitespace_for_result = qty_lines - len(str(result))
        iteration += 1
        if answer == 'y':
            myTab.add_column(columns[0], [" "+" " * qty_whitespace1 + str(first_number), operator + " " * qty_whitespace2 + str(second_number), "-" * qty_lines, " " * qty_whitespace_for_result + str(result)])
        else:
            myTab.add_column(columns[0], [" " + " " * qty_whitespace1 + str(first_number),
                                      operator + " " * qty_whitespace2 + str(second_number), "-" * qty_lines])

    print(myTab)

def qty_whitespace(expression):  #
    qty_for_digit1, qty_for_digit2 = 1, 1  # начальное количество пробелов
    expr_split = (expression.split())  # разбиваю на части выражение

    first_number = expr_split[0]
    second_number = expr_split[2]
    if len(first_number) > len(second_number):  # если длина первого числа больше второго
        qty_for_digit2 = len(first_number) - len(
            expr_split[2]) + 1  # вычисляю сколько пробелов добавить перед вторым числом
        return qty_for_digit1, qty_for_digit2  # возвращяю количество пробелов
    elif len(first_number) < len(second_number):  # если длина первого числа меньше второго
        qty_for_digit1 = len(second_number) - len(
            first_number) + 1  # вычисляю сколько пробелов добавить перед первым числом
        return qty_for_digit1, qty_for_digit2  # возвращяю количество пробелов
    else:  #
        return qty_for_digit1, qty_for_digit2  # если равны возвращяю количество пробелов


while 1:
    answer = input('Print result? y/n')
    if answer == 'y' or answer == 'n':
        arithmetic_arranger(expressions, answer=answer)
        break
    else:
        print('Enter y or n')

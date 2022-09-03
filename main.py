# Scientific computing with python

expressions = ['1 + 1', '1 + 10', '10 + 2', '3 * 100', '40000 + 200', '1500 - 1000']
operator = '-+'


def arithmetic_arranger(expressions, answer): # Вычисление выражений
    result = 0
    iteration = 1
    for expression in expressions: # Выбирается по одному выражению из списка выражений
        print(f'expession {iteration}')
        if operator[0] or operator[1] in expression: # Нахожу + или -
            expr_split = (expression.split()) # разбиваю выражение
            if len(expr_split[0]) > 4 or len(expr_split[2]) > 4:
                print('    Error: Numbers cannot be more than four digits.')
                continue
            elif '+' in expr_split: # если в выражении плюс,
                result = int(expr_split[0]) + int(expr_split[2]) # то складываю числа
            elif '-' in expr_split: # если в выражении -,
                result = int(expr_split[0]) - int(expr_split[2])#  то вычитаю

            qty_whitespace1, qty_whitespace2 = qty_whitespace(expression)  # нахожу количество пробелов для вывода на экран выражения в столбик
            print(
                f' {" " * qty_whitespace1}{expr_split[0]}\n{expr_split[1]}{" " * qty_whitespace2}{expr_split[2]}') # печать выражения
            qty_lines = 1 + qty_whitespace2 + len(expr_split[2])
            qty_whitespace_for_result = qty_lines - len(str(result))
            print("-" * qty_lines) # количество черточек
            if answer == 'y':
                print(f'{" " * qty_whitespace_for_result}{result}')  # вывод результата, усли нужен
            elif answer == 'n':
                print('')
            iteration += 1
        elif operator[0] not in expression or operator[1] not in expression:
            print('Error: Operator must be "+" or "-".')
            break


def qty_whitespace(expression): #
    qty_for_digit1, qty_for_digit2 = 1, 1 # начальное количество пробелов
    expr_split = (expression.split()) # разбиваю на части выражение
    if len(expr_split[0]) > len(expr_split[2]): # если длина первого числа больше второго
        qty_for_digit2 = len(expr_split[0]) - len(expr_split[2]) + 1 # вычисляю сколько пробелов добавить перед вторым числом
        return qty_for_digit1, qty_for_digit2 # возвращяю количество пробелов
    elif len(expr_split[0]) < len(expr_split[2]): # если длина первого числа меньше второго
        qty_for_digit1 = len(expr_split[2]) - len(expr_split[0]) + 1 # вычисляю сколько пробелов добавить перед первым числом
        return qty_for_digit1, qty_for_digit2 # возвращяю количество пробелов
    else: #
        return qty_for_digit1, qty_for_digit2 # если равны возвращяю количество пробелов


while True:
    answer = input('Print result? y/n, or q for exit')
    if answer == 'y' or answer == 'n':
        arithmetic_arranger(expressions, answer)
    elif answer == 'q':
        break
    else:
        print('Enter y or n')


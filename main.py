# Scientific computing with python

expressions = ['4000 + 20', '150 - 10']
answer = 'n'
chars = '-+'


def arithmetic_arranger(expressions):
    result = 0
    for expression in expressions:
        if chars[0] or chars[1] in expression:
            expr_split = (expression.split())
            if '+' in expr_split:
                result = int(expr_split[0]) + int(expr_split[2])
            elif '-' in expr_split:
                result = int(expr_split[0]) - int(expr_split[2])
            qty_whitespace1, qty_whitespace2 = qty_whitespace(expression)
            print(
                f'{" " * qty_whitespace1}{expr_split[0]}\n{expr_split[1]}{" " * qty_whitespace2}{expr_split[2]}')
            print(qty_whitespace1, qty_whitespace2)
            print("-" * (3 + abs(qty_whitespace1 - qty_whitespace2)))
            print_result(result)
        else:
            print('no -+')


def qty_whitespace(expression):
    qty_for_digit1, qty_for_digit2 = 1, 1
    expr_split = (expression.split())
    if len(expr_split[0]) > len(expr_split[2]):
        qty_for_digit2 = len(expr_split[0]) - len(expr_split[2])
        return qty_for_digit1, qty_for_digit2
    elif len(expr_split[0]) < len(expr_split[2]):
        qty_for_digit1 = len(expr_split[2]) - len(expr_split[0])
        return qty_for_digit1 + 2, qty_for_digit2
    else:
        return qty_for_digit1 + 1, qty_for_digit2


def print_result(answer):
    if answer == 'y':
        return print(arithmetic_arranger(expressions))
    elif answer == 'n':
        return print('')
    else:
        print('Enter y or n')


arithmetic_arranger(expressions)
answer = input('Print result? y/n')
print_result(answer)

# Scientific computing with python

expressions = ['25 + 10000', '150 - 10']
answer = True
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
            print(f'{expr_split[0]}\n{expr_split[1]} {expr_split[2]}')
            print('result', result)
        else:
            print('no -+')


arithmetic_arranger(expressions)

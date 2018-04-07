import math

cases = int(input())
i = 0
while i < cases:
    number = float(input())
    if number < 2 ** (1 / 2):
        arc_cos = math.acos(1 / number)
        number = math.cos(arc_cos) / 2
    print('Case #' + str(i + 1) + ':')
    print(str(number) + ' ' + str(number) + ' 0')
    print('-' + str(number) + ' ' + str(number) + ' 0')
    print('0 0 0.5')
    i += 1

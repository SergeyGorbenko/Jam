import math

cases = int(input())
i = 0
while i < cases:
    number = float(input())
    if number < 2 ** (1 / 2):
        number = number / 2
        arc_cos = math.acos(number / ((math.sqrt(2) / 2)))
        angle = arc_cos + ((math.pi * 45) / 180)
        print('Case #' + str(i + 1) + ':')
        print(str(math.sin(angle) / 2) + ' ' + str(math.cos(angle) / 2) + ' 0')
        print(str(0 - (math.cos(angle) / 2)) + ' ' + str(math.sin(angle) / 2) + ' 0')
        print('0 0 0.5')
    else:
        angle = (math.pi * 45) / 180
        shadow = math.sqrt(number * 2 / 3 / math.sqrt(3))
        a = math.sqrt(math.pow(shadow, 2) - 0.5)
        alpha = math.acos((a + shadow / 2) / math.sqrt(2))
        print('Case #' + str(i + 1) + ':')
        print(str(math.sin(angle) / 2 - math.sin(alpha) / 2) + ' ' + str(math.cos(angle) / 2) + str(math.cos(alpha) / 2))
        print(str(0 - (math.sin(angle) / 2) + math.sin(alpha) /2 ) + ' ' + str(math.cos(angle) / 2) + str(0 - math.cos(alpha) / 2))
        print(str(math.sin(alpha) / 2) + ' ' + '0 ' + str(math.cos(alpha) / 2))

    i += 1

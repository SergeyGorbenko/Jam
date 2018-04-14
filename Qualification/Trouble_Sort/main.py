cases = int(input())
i = 0
while i < cases:
    number = int(input())
    list = input().split()
    list = [int(i) for i in list]
    done = True
    while done:
        done = False
        j = 0
        while j < list.__len__() - 2:
            if list[j] > list[j + 2]:
                done = True
                list[j], list[j + 2] = list[j + 2], list[j]
            j += 1
    j = 0
    if_wrong = True
    while j < number - 1:
        if list[j] > list[j + 1]:
            print('Case #' + str(i + 1) + ': ' + str(j))
            if_wrong = False
            break
        j += 1
    if if_wrong:
        print('Case #' + str(i + 1) + ': OK')
    i += 1

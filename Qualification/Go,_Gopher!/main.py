T = int(input())  # cases

place = []

for i in range(1, T + 1):
    A = (int(input()))  # area
    a = A // 9
    mod_a = A % 9
    x = y = 13
    count = 0
    for j in range(1000):
        if place.__len__() == 9:
            place.clear()
            count += 1
            if count == a and mod_a != 0:
                x += mod_a // 3 + 1
            elif count == a and mod_a == 0:
                break
            else:
                x += 3

        print(x, y)
        s = str(input()).split()
        if place.__contains__(s):
            continue
        place.append(s)
        if int(s[0]) == 0 and int(s[1]) == 0:  # successful
            break

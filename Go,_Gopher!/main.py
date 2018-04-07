T = int(input())

for i in range(1, T + 1):
    place = []
    A = int(input())
    x = y = 13
    for j in range(1000):
        print()
        s = [int(p) for p in input().split()]
        place.append(s)
        if s[0] == 0 and s[1] == 0:             # successful
            break

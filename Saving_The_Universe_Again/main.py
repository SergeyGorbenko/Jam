T = int(input())


def Kick(ls):
    push = 0
    strange = 1
    for c in ls:
        if c == 'C':
            strange = strange << 1
        else:
            push += strange
    return push


def check(ls, lst):
    try:
        while ls[lst] == 'S':
            lst -= 1
    except IndexError:
        print('IMPOSSIBLE')
        return False
    return lst


for i in range(1, T + 1):
    D = int(input())
    P = list(input())
    len_P = P.__len__()

    hack = 0
    last = -1
    r = True
    while Kick(P) > D:
        last = P[::-1].index('S')
        last = check(P, len_P - last - 1)
        if (not last) and last != 0:
            r = False
            break
        P[last], P[last + 1] = P[last + 1], P[last]
        hack += 1

    if not r:
        continue
    print('Case #{}: {}'.format(i, hack))

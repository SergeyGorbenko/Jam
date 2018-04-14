T = int(input())
# S*N+P
for i in range(1, T + 1):
    case = []
    R, B, C = [int(x) for x in input().split()]
    n = B // R
    if B % R != 0:
        n += 1
    for j in range(C):
        M, S, P = [int(x) for x in input().split()]
        case.append([M, S, P, M * S + P])
    case.sort(key=lambda i:i[3])
    count = 1
    x = case[0]
    for l in range(case.__len__()):
        if case[l][3] == x[3]:
            continue
        count+=1
        if count == B+1:
            count = l
            break
    case = case[:count]
    case.sort(key=lambda i: i[1])
    print(case)
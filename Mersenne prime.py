from math import sqrt
n = 0
S = []
for i in range(2, int(10e3)):  # change range value for more outputs
    flag = 1
    k = int(sqrt(i))
    for j in range(2, k+1):
        if i % j == 0:
            flag = 0
            break
    if flag:
        S.append(i)
        #print(i, end=' ')

#S = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for M in S:
    for P in S:
        if 2 ** M - 1 == P:
            print(M, P)
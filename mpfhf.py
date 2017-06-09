#!/usr/bin/env python
from sys import argv

def stringify(field):
    return ''.join(map(str, field))

def flip(field, index):
    field[index] = 0 if field[index] == 1 else 1

def invert(field):
    for i in range(0, len(field)):
        flip(field, i)

def screw(a, b, M, M_pos, half):
    count = len(a)/2 if half else len(a)
    for i in range(0, len(a)):
        flip(b, ((a[i] * M_pos) % len(b)))

message = argv[1]
R_len = int(argv[2])

M = map(int, ''.join(map(lambda p: format(p, 'b'), map(ord, message))))
S = [0]
R = [0] * R_len

for i in range(0, len(M)):
    if M[i] == 0:
        S.append(0)
        screw(S, R, M, i, False)
        flip(R, i%R_len)
        if [i%R_len] == 0:
            i -= 1
        else:
            invert(S)
    if M[i] == 1:
        screw(S, R, M, i, True)
        S_len = len(S)
        if R[i%R_len] == S[i%S_len]:
            screw(S, R, M, i, False)
        else:
            flip(R, i%R_len)

print(stringify(R))

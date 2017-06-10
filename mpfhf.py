#!/usr/bin/env python
from sys import argv

def stringify(field):
    return ''.join(map(str, field))

def flip(field, index):
    field[index] = 0 if field[index] == 1 else 1

def invert(field):
    for i in range(0, len(field)):
        flip(field, i)

def screw(a, b, M_pos, half):
    count = len(a)/2 if half else len(a)
    for i in range(0, count):
        flip(b, ((i * M_pos) % len(b)))

def expand():
    S.append(0)

message = argv[1]
R_len = int(argv[2])

M = list(map(int, ''.join(map(lambda p: format(p, 'b'), map(ord, message)))))
S = [0]
R = [0] * R_len
M_pos = 0
step = 0

while M_pos < len(M):
    if M[M_pos] == 0:
        expand()
        screw(S, R, M_pos, False)
        if R[M_pos%R_len] == 0:
            flip(R, M_pos%R_len)
            if M_pos != 0: M_pos -= 1
        else:
            flip(R, M_pos%R_len)
            invert(S)
    else:
        screw(S, R, M_pos, True)
        if R[M_pos%R_len] == S[M_pos%len(S)]:
            expand()
            screw(R, S, M_pos, False)
        else:
            flip(R, M_pos%R_len)
    M_pos += 1
    step += 1

print(stringify(R))

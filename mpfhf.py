#!/usr/bin/env python
from time import time
from sys import argv

def get_time():
    return int(round(time() * 1000))

def stringify(field):
    return ''.join(map(str, field))

def flip(field, index):
    field[index] = 0 if field[index] == 1 else 1

def invert(field):
    for i in range(0, len(field)):
        flip(field, i)

def screw(a, b, half):
    count = len(a)/2 if half else len(a)
    for i in range(0, count):
        flip(b, ((i * M_pos) % len(b)))

def expand():
    S.append(0)

print_time = False

if len(argv) < 4:
    print("Usage: python mpfhf.py <message> <hashlength> <time|notime>")
    exit(1)

message = argv[1]
R_len = int(argv[2])

if argv[3] == "time":
    print_time = True

M = list(map(int, ''.join(map(lambda p: '{0:08b}'.format(p, 'b'), map(ord, message)))))
start_time = get_time()
S = [0]
R = [0] * R_len
M_pos = 0
step = 0

while M_pos < len(M):
    if M[M_pos] == 0:
        expand()
        screw(S, R, False)
        if R[M_pos%R_len] == 0:
            flip(R, M_pos%R_len)
            if M_pos != 0: M_pos -= 1
        else:
            flip(R, M_pos%R_len)
            invert(S)
    else:
        screw(S, R, True)
        if R[M_pos%R_len] == S[M_pos%len(S)]:
            expand()
            screw(R, S, False)
        else:
            flip(R, M_pos%R_len)
    M_pos += 1
    step += 1

if print_time:
    print(get_time() - start_time)
print(stringify(R))

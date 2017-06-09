#!/usr/bin/env python
from sys import argv

DEBUG = True

def debug(message):
    if DEBUG:
        print message

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

print "Message: %s" % message
print "Result ring size: %d" % R_len
print "M: %s" % stringify(M)
print "S: %s" % stringify(S)
print "R: %s" % stringify(R)

for i in range(0, len(M)):
    debug("--------------------------------------------------------------------------------------------------------------------")
    debug("Step %d:" % (i+1))
    debug("We find ourselves at position %d in M, that bit is %d." % (i, M[i]))
    if M[i] == 0:
        debug("Because the bit is 0, we add a null bit to the state machine, which now becomes:")
        S.append(0)
        debug("S = %s." % stringify(S))
    if M[i] == 1:
        debug("Because the bit is 1, we flip the M%S-th, 2M%S-th, ... nM%S-th bits in S, where n=len(S)/2")
        screw(S, R, M, i, True)
        debug("S = %s." % stringify(S))

        S_len = len(S)
        debug("As R is %d bits long and we are on position %d, we take the %d-th bit of R, which is %d and we compare it to the %d-th bit of S, which is %d." % (R_len, i, i%R_len, R[i%R_len], i%S_len, S[i%S_len]))
        if R[i%R_len] == S[i%S_len]:
            screw(S, R, M, i, False)
        else:
            debug("Because they don't match we flip the M%S-th, 2M%S-th, ... nM%S-th bits in R. R becomes:")
            flip(R,i%R_len)
            print stringify(R)

    break

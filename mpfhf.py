#!/usr/bin/env python
from sys import argv

def debug(message):
    if DEBUG:
        print(message)

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

DEBUG = False
message = argv[1]
R_len = int(argv[2])
if len(argv) == 4 and argv[3] == "debug":
    DEBUG = True

M = map(int, ''.join(map(lambda p: format(p, 'b'), map(ord, message))))
S = [0]
R = [0] * R_len

debug("Message: %s" % message)
debug("R_len: %d" % R_len)
debug("M: %s" % stringify(M))
debug("S: %s" % stringify(S))
debug("R: %s" % stringify(R))

for i in range(0, len(M)):
    debug("\nStep %d:" % (i+1))
    debug("We find ourselves at position %d in M, that bit is %d." % (i, M[i]))
    if M[i] == 0:
        debug("Because the bit is 0:")
        debug("\tWe expand S:")
        S.append(0)
        debug("\tS = %s," % stringify(S))
        debug("\tand then screw S in R:")
        screw(S, R, M, i, False)
        debug("\tR = %s," % stringify(R))
        debug("\tand then flip the M_pos%R_len-th bit in R:")
        flip(R, i%R_len)
        debug("\tR = %s," % stringify(R))
        debug("\tWe check to see if the M_pos%R_len-th bit in R is 0:")
        if R[i%R_len] == 0:
            debug("\t\tIt is, so we rewind by one.")
            i -= 1
        else:
            debug("\t\tIt isn't, so we invert S:")
            invert(S)
            debug("\tS = %s." % stringify(S))
    if M[i] == 1:
        debug("Because the bit is 1:")
        debug("\tWe halfscrew S in R:")
        screw(S, R, M, i, True)
        debug("\tR = %s," % stringify(R))
        S_len = len(S)
        debug("\tWe compare the M_pos%R_len-th bit of R with the M_pos%R_len-th bit of S:")
        if R[i%R_len] == S[i%S_len]:
            debug("\t\tBecause they match, we screw S in R:")
            screw(S, R, M, i, False)
            debug("\t\tR = %s." % stringify(R))
        else:
            debug("\t\tBecause they don't match, we flip the M_pos%R_len-th bit of R:")
            flip(R, i%R_len)
            debug("\t\tR = %s." % stringify(R))

if DEBUG:
    debug("Our work has ended. The message was:")
    debug(stringify(M))
    debug("We used %d bits for the state machine." % len(S))
    debug("The resulting hash is:")
print(stringify(R))

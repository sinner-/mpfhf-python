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

def screw(a, b, M_pos, half):
    count = len(a)/2 if half else len(a)
    for i in range(0, len(a)):
        flip(b, ((i * M_pos) % len(b)))

def expand():
    S.append(0)

DEBUG = False
message = argv[1]
R_len = int(argv[2])
if len(argv) == 4 and argv[3] == "debug":
    DEBUG=True

M = map(int, ''.join(map(lambda p: format(p, 'b'), map(ord, message))))
S = [0]
R = [0] * R_len

debug("Message: %s" % message)
debug("R_len: %d" % R_len)
debug("M: %s" % stringify(M))
debug("S: %s" % stringify(S))
debug("R: %s" % stringify(R))

step = 1
M_pos = 0
while M_pos < len(M):
    debug("\nStep %d" % (step))
    debug("We find ourselves at position %d in M, that bit is %d." % (M_pos, M[M_pos]))
    if M[M_pos] == 0:
        debug("Because the bit is 0:")
        debug("\tWe expand:")
        expand()
        debug("\tS = %s." % stringify(S))
        debug("\tWe screw S in R:")
        screw(S, R, M_pos, False)
        debug("\tR = %s." % stringify(R))
        debug("\tWe check to see if the M_pos%R_len-th bit in R is 0:")
        if R[M_pos%R_len] == 0:
            debug("\tBecause the M_pos%R_len-th bit in R is 0:")
            debug("\t\tWe flip the M_pos%R_len-th bit in R:")
            flip(R, M_pos%R_len)
            debug("\t\tR = %s." % stringify(R))
            if M_pos != 0:
                debug("\t\tM_pos is not 0, so we rewind.")
                M_pos -= 1
        else:
            debug("\tBecause the M_pos%R_len-th bit in R is 1:")
            debug("\t\tWe flip the M_pos%R_len-th bit in R:")
            flip(R, M_pos%R_len)
            debug("\t\tR = %s." % stringify(R))
            debug("\t\tWe invert S:")
            invert(S)
            debug("\t\tS = %s." % stringify(S))
    else:
        debug("Because the bit is 1:")
        debug("\tWe halfscrew S in R:")
        screw(S, R, M_pos, True)
        debug("\tR = %s." % stringify(R))
        S_len = len(S)
        debug("\tWe compare the M_pos%R_len-th bit in R with the M_pos%R_len-th bit in S:")
        if R[M_pos%R_len] == S[M_pos%S_len]:
            debug("\tBecause the bits match:")
            debug("\t\tWe expand:")
            expand()
            debug("\t\tS = %s." % stringify(S))
            debug("\t\tWe screw R in S:")
            screw(R, S, M_pos, False)
            debug("\t\tS = %s." % stringify(S))
        else:
            debug("\tBecause the bits match")
            debug("\t\tWe flip the M_pos%R_len-th bit in R:")
            flip(R, M_pos%R_len)
            debug("\t\tR = %s." % stringify(R))
    M_pos += 1
    step += 1

if DEBUG:
    debug("\nOur work has ended, in %d steps and using %d bits for the state machine." % (step, len(S)))
    debug("The message was:\n%s" % stringify(M))
    debug("The resulting hash is:") 
print(stringify(R))

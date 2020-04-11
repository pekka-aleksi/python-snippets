import string
from collections import deque

alphabet = string.ascii_lowercase + " "

Q = deque(alphabet)
Q.rotate(-3)

word = "this is a caesar cypher"

for ch in word:
    q_ind = alphabet.index(ch)
    print(ch, Q[q_ind])

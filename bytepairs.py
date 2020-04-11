from collections import Counter as c

counter = 0

# this implements bytepairs but doesn't really compress text

def forward(s, repl=dict()):
    global counter

    cstring = "{:>3}".format(counter)

    bytepairs = ["{}{}".format(first, s[i + 1]) for i, first in enumerate(s[0:-1]) if
                 not first.isdigit() and not s[i + 1].isdigit()]

    C = c(bytepairs)

    most_common_bytepair, most_common_count = C.most_common(1)[0]

    if most_common_count == 1:  # this is the end of the recursion
        return s, repl

    # here we continue the recursion because we have stuff to do still

    s = s.replace(most_common_bytepair, cstring)

    repl[cstring] = most_common_bytepair
    counter += 1

    return forward(s)


def backward(data):
    s, d = data

    for k, val in sorted(d.items(), reverse=True):
        s = s.replace(k, val)

    return s


if __name__ == '__main__':
    start = """This an incoming text which will get encoded as bytepairs"""

    print(start)
    encoded = forward(start)
    print(encoded)
    decoded = backward(encoded)
    print(decoded)

    assert decoded == start

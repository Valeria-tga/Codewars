import string


def is_pangram(s):
    alphavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    k = 0
    for i in range(len(s)):
        s = s.replace(s[i], s[i].lower())

    for i in range(len(alphavit)):
        if alphavit[i].lower() in s:
            k = k + 1
            s = s.replace(alphavit[i], '')
    if k == 26:
        result = True
    else:
        result = False
    return result
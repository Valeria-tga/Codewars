# The main idea is to count all the occurring characters in a string.
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#
# What if the string is empty? Then the result should be empty object literal, {}.

s='aba'

def count(s):
    a={}
    for i in s:
        if i not in a:
            a[i]=s.count(i)
    return a

print(count(s))



# decision1
# from collections import Counter
#
# def count(string):
#     return Counter(string)


# decision 2
# def count(string):
#     return {i: string.count(i) for i in string}


# decision3
# def count(string):
#     counter = {}
#     for char in string:
#         counter[char] = counter.get(char, 0) + 1
#     return counter


# decision4
# def count(s):
#     return {x:s.count(x) for x in set(s)}
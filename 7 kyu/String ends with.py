# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

#Мое решение

def solution(string, ending):
    if string[len(string)-len(ending):] == ending:
        return True
    else:
        return False

# Отладка:

condition=('abcde', 'abc')
# print(len(condition[1]))
# print(condition[0][len(condition[0])-len(condition[1]):])

if condition[0][len(condition[0])-len(condition[1]):] == condition[1]:
    print(True)
else:
    print(False)

# Другие решения:
#1
def solution(string, ending):
    return string.endswith(ending)

#2
solution = str.endswith

#3

def solution(string, ending):
    return ending in string[-len(ending):]
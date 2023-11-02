# Introduction
# The first century spans from the year 1 up to and including the year 100,
# the second century - from the year 101 up to and including the year 200, etc.
#
# Task
# Given a year, return the century it is in.
#
# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

# Note: this kata uses strict construction as shown in the description and the examples,
# you can read more about it here


def centure(year):
    if year<100:
        return f'1'
    else:
        result=year//100
        if result*100<year:
            result=result+1
            return result
        else:
            return result

print(centure(2108))

# decision 1
# def century(year):
#     return (year + 99) // 100

# decision 2
# import math
#
# def century(year):
#     return math.ceil(year / 100)

# decision 3
# def century(year):
#     if year%100==0:
#         return year//100
#     else:
#         return year//100+1
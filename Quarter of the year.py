# Given a month as an integer from 1 to 12, return to which quarter of the year
# it belongs as an integer number.
#
# For example: month 2 (February), is part of the first quarter; month 6 (June),
# is part of the second quarter; and month 11 (November), is part of the fourth quarter.
#
# Constraint:
#
# 1 <= month <= 12


def quarter_of(month):
    if month>9:
        return 4
    elif month>6:
        return 3
    elif month>3:
        return 2
    else:
        return 1

print(quarter_of(9))

# decision 1
# from math import ceil
# def quarter_of(month):
#     return ceil(month / 3)


# decision 2
# def quarter_of(n):
#     return (n + 2) // 3



# Trolls are attacking your comment section!
#
# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
#
# Your task is to write a function that takes a string and return a new string with all vowels removed.
#
# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
#
# Note: for this kata y isn't considered a vowel.

# s='This website is for losers LOL!'
# result=''
# vowels=('e','i','u','a','o')
# s=s.lower()
# print(s)
#
# for i in s:
#     if i in vowels:
#         k=s.index(i)
#         print(i)
#         result=result+s[:k]
#         s = s[k + 1:]
# result=result+s
# print(result)


def disemvowel(string_):
    result=''
    vowels=('e','i','u','a','o','E','I','U','A','O')
    for i in string_:
        if i in vowels:
            k=string_.index(i)
            result=result+string_[:k]
            string_ = string_[k + 1:]
    result=result+string_
    return result
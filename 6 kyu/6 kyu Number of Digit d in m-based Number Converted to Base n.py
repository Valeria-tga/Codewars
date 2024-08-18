
def count_digit(number, digit, base=10, from_base=10):
    digit=str(digit)
    if base==10 and from_base==10:
        print(number, digit, str(number).count(digit))
        return str(number).count(digit)
    elif base==10 and from_base!=10:
        number=in_ten_base(number,from_base)
        print(number, digit, str(number).count(digit))
        return str(number).count(digit)
    elif base!=10 and from_base==10:
        number=from_ten_base(number,base)
        print(number, digit, str(number).count(digit))
        return str(number).count(digit)
    elif base!=10 and from_base!=10:
        number=in_ten_base(number,from_base)
        print('В десятичной СС: ',in_ten_base(number,from_base))
        number=from_ten_base(number,base)
        print(number, digit,str(number).count(digit))
        return str(number).count(digit)
def from_ten_base(number,base):
    # num_str=str(number)
    result=''
    dict={
        10:'a', 11:'b', 12:'c', 13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j',20:'k', 21:'l', 22:'m', 23:'n',24:'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u', 31:'v', 32:'w', 33:'x',34:'y',35:'z'
    }
    while int(number)>0:
        fact=int(number)%base
        if fact>9:
            for i in dict.keys():
                if i==fact:
                    fact=dict[i]
                    result=fact+result
        else:
            result=str(int(number)%base)+result
        number=int(number)//base
    return result

def in_ten_base(number,base):
    num_str=str(number)
    num_str=num_str[::-1]
    dict = {
        10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l',
        22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x',
        34: 'y', 35: 'z'
    }
    # print(dict.values())
    dict_list=list(dict.items())
    result=0
    for i in range(len(num_str)):
        if num_str[i] in dict.values():
            k=0
            for j in dict.values():
                k+=1
                if i==j:
                    fact=int(dict_list[k][0])
                    # print(fact)
                    result=fact+result
        else:
            result=result+int(num_str[i]) * base ** i
    # print(result)
    return result



print('result = ',count_digit("7i98chihe1", "1", 17, 22))
#
# print(123%9)
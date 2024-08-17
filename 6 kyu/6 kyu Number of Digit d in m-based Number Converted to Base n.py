
def count_digit(number, digit, base=10, from_base=10):
    digit=str(digit)
    if base==10 and from_base==10:
        return str(number).count(digit)
    elif base==10 and from_base!=10:
        number=in_ten_base(number,from_base)
        return str(number).count(digit)
    elif base!=10 and from_base==10:
        number=from_ten_base(number,base)
        return str(number).count(digit)
    elif base!=10 and from_base!=10:
        number=in_ten_base(number,from_base)
        number=from_ten_base(number,base)
        return str(number).count(digit)
def from_ten_base(number,base):
    # num_str=str(number)
    result=''
    dict={
        10:'a', 11:'b', 12:'c', 13:'d',14:'e',15:'f',16:'g',17:'h',18:'i',19:'j'
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
    result=0
    for i in range(len(num_str)):
        result=result+int(num_str[i]) * base ** i
    # print(result)
    return result



print(count_digit("1100101110101", "d", 15, 2))

# print(123%9)
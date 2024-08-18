# Sort the given array of strings in alphabetical order, case insensitive. For example:
#
# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]


# list=["C", "d", "a", "B"]
# list=["Hello", "there", "I'm", "fine"]
list=['a', 'come', 'Case', 'find', 'group', 'It', 'Last', 'Long', 'Own', 'point', 'public', 'see', 'Small', 'They', 'Time', 'up']
# print(ord(list[1].lower()))
#Sort choice
if len(list[0])<=1:
    for i in range(len(list)):
        min_lower = ord(list[i].lower())
        min=ord(list[i])
        ind=i
        for j in range(i+1,len(list)):
            if ord(list[j].lower())<min_lower:
                min=ord(list[j])
                min_lower = ord(list[j].lower())
                ind=j
        temp=list[i]
        list[i]=chr(min)
        list[ind]=temp
else:
    for i in range(len(list)):
        min_lower = ord(list[i][0].lower())
        min=list[i]
        ind=i
        for j in range(i+1,len(list)):
            if ord(list[j][0].lower())<min_lower:
                min=list[j]
                min_lower = ord(list[j][0].lower())
                ind=j
        temp=list[i]
        list[i]=min
        list[ind]=temp
print(list)

# ['a', 'come', 'Case', 'find', 'group', 'It', 'Last', 'Long', 'Own', 'point', 'public', 'see', 'Small', 'They', 'Time', 'up']
# should equal ['a', 'Case', 'come', 'find', 'group', 'It', 'Last', 'Long', 'Own', 'point', 'public', 'see', 'Small', 'They', 'Time', 'up']
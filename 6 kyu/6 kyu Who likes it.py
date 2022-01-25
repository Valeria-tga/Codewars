#likes([]) # must be "no one likes this"
#likes(["Peter"]) # must be "Peter likes this"
#likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
#likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
#likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

pattern1=' likes this'
pattern2=' like this'
list=["Alex", "Jacob", "Mark", "Max"]

if list==[]:
    print('no one' + pattern)

if len(list)==1:
    print(list[0]+pattern1)

if len(list)==2:
    print(list[0]+' and '+list[1]+pattern2)

if len(list)==3:
    print(list[0]+', '+list[1]+' and '+list[2]+pattern2)

if len(list)>3:
    k=len(list)-2
    print(list[0]+', '+list[1]+' and ',k,' others '+pattern2)


def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.

    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others=length - 2)

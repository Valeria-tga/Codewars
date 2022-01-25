string='123'
chisla=['0','1','2','3','4','5','6','7','8','9']
k=False

if len(string)==4 or len(string)==6:
    for i in range(0,len(string)):
        print(i)
        if string[i] not in chisla:
            print(string[i])
            k=True
else:
    k=True

if k==True:
    print(False)
else:
    print(True)

#Или такой код:

#def validate_pin(pin):
#   return len(pin) in (4, 6) and pin.isdigit()


# Или такой код:

#def validate_pin(pin):
#    return len(pin) in [4, 6] and pin.isdigit()

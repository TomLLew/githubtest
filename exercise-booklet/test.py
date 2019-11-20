x = float(input('enter num 1:  '))
y = float(input('enter num2:   '))
z = bool(input('true for add false for multiply:   '))



def method(x, y, z):
    if z == True:
        return x + y
    elif z == False:
        return x * y

print(method(x, y, z))





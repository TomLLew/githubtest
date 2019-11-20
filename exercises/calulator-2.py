def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

operator = '1234'

i = True

while i == True:
    
    x = float(input('enter number:  '))

    print('please select a option:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide')

    method = str(input('what do you want to do?   '))
            
    y = float(input('enter number:  '))


    if method == 1:
        print(x, ' + ', y, '\n=', add(x,y))

    elif method == 2:
        print(x, ' + ', y, '\n=', subtract(x,y))

    elif method == 3:
        print(x, ' + ', y, '\n=', multiply(x,y))

    elif method == 4:
        print(x, ' + ', y, '\n=', divide(x,y))


def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

while True:
    
    x = float(input('enter number:  '))
    
    y = float(input('enter number:  '))

    print('please select a option:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide')

    method = int(input('what do you want to do?   '))

    if method == 1:
        print(x, ' + ', y, '\n=', add(x,y))

    elif method == 2:
        print(x, ' - ', y, '\n=', subtract(x,y))

    elif method == 3:
        print(x, ' * ', y, '\n=', multiply(x,y))

    elif method == 4:
        print(x, ' / ', y, '\n=', divide(x,y))

    else:
        print('sorry wrong input\n use 1 for add and so on')
        continue

    retry = input('do you want to go again (y/n)?   ')
    
    retry.lower()
    
    if retry == 'y':
        exit
      
    elif retry == 'n':
        print('enjoy your day')
        break

    else:
        print('wrong input try again')
          


    

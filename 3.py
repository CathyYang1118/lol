symbol = input('Input a symbol:')

while True:
    num = int(input('Input an odd number:'))
    if num%2 != 0:
        break
    
NumberOfSpaces = int((num-1)/2)
NumberOfSymbol = 1
space = 1

while True:
    if NumberOfSymbol == 1:
        for i in range(NumberOfSpaces):
            print(' ',end = '')
        print(symbol)
    elif NumberOfSymbol >= 1:
        for j in range (NumberOfSpaces):
            print(' ',end='')
        print(symbol,end ='')
        print(' '*space,end = '')
        print(symbol)
        space += 2
    
    NumberOfSpaces -= 1
    NumberOfSymbol += 2
        
    if NumberOfSymbol == num:
        for k in range(num):
            print(symbol,end='')
        break


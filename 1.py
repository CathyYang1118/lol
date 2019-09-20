symbol = input('Input a symbol:')

while True:
    num = int(input('Input an odd number:'))
    if num%2 != 0:
        break
    
NumberOfSpaces = int((num-1)/2)
NumberOfSymbol = 1

while True:
    for i in range(NumberOfSpaces):
        print(' ',end = '')
    for j in range(NumberOfSymbol):
        print(symbol, end = '')
    print('')
    NumberOfSpaces -= 1
    NumberOfSymbol += 2
    
    if NumberOfSymbol > num:
        break

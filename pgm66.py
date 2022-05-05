# Year between limits and its Leap year or not
a=int(input('a='))
b=int(input('b='))
while a<=b:
    print(a)
    if a%4==0:
             print('Leap year')
    else:
        print('Not leap year')
a=a+1
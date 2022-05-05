# Number between limits and its Even or Odd
a=int(input('a='))
b=int(input('b='))
while a<=b:
    print(a)
if a%2==0:
    print('Even')
else:
    print('Odd')
a=a+1
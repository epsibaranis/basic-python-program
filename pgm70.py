#Sum of Positive and Negative nos other than 1000
c=int(input('c=?'))
x=0
y=0
while c!=1000:
    print(c)
    if c>0:
        x=x+c
    else:
        y=y+c
    c=int(input('c=?'))
print(x,y)    
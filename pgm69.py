# Count the number of positive, negative, zero other than 1000
c=int(input('c=?'))
x=0
y=0
z=0
while c!=1000:
    print(c)
    if c>0:
        x=x+1
    elif c<0:
        y=y+1
    else:
        z=z+1
    c=int(input('c=?'))
print(x,y,z)    


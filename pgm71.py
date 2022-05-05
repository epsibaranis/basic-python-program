#average of positive and negatie no other than 1000
c=int(input("c=?"))
a=0
b=0
c=0
d=0
f=0
while c!=1000:
    print(c)
    if c>0:
        a=a+1
        b=b+c
    else:
        d=d+1
        f=f+c
        c=int(input("c=?"))
print(a/b,d/f)
            

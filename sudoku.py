import random
l=[1,2,3,4,5,6,7,8,9,]
c1,c2,c3,c4,c5,c6,c7,c8,c9=[],[],[],[],[],[],[],[],[]
r1,r2,r3,r4,r5,r6,r7,r8,r9=[],[],[],[],[],[],[],[],[]
#grid 1,2,3

def grid_1(x1,x2,x3,c):
    l=[1,2,3,4,5,6,7,8,9]
    r=0
    def add_remove(x):

        a=random.choice(l)
        if a not in x:
            x.append(a)
            l.remove(a)

        return x

    while l:
        if len(x1)!=c:
            x1=add_remove(x1)
        elif len(x2)!=c:
            x2=add_remove(x2)
        elif len(x3)!=c:
            x3=add_remove(x3)
    return x1,x2,x3


r1,r2,r3=grid_1(r1,r2,r3,3)
r1,r2,r3=grid_1(r1,r2,r3,6)
r1,r2,r3=grid_1(r1,r2,r3,9) 

def col(x1,x2,x3,y1,y2,y3,l,u):
    for a in range(l,u):
        if a==l:
            y1.append(x1[a])
            y1.append(x2[a])
            y1.append(x3[a])
        elif a==l+1:
            y2.append(x1[a])
            y2.append(x2[a])
            y2.append(x3[a])
        else:
            y3.append(x1[a])
            y3.append(x2[a])
            y3.append(x3[a])

    return  y1,y2,y3

c1,c2,c3=col(r1,r2,r3,c1,c2,c3,0,3)
c4,c5,c6=col(r1,r2,r3,c4,c5,c6,3,6)
c7,c8,c9=col(r1,r2,r3,c7,c8,c9,6,9)

print(r1)
print(r2)
print(r3)



#grid 4,5,6
def grid_2(x4,x5,x6,c,y4,y5,y6,k):
    l=[1,2,3,4,5,6,7,8,9]

    def add_remove(x,y4,y5,y6,k):
        a=random.choice(l)
        if a not in x:
            if len(x)==k:
                if a not in y4:
                    x.append(a)
                    l.remove(a)
            elif len(x)==k+1:
                if a not in y5:
                    x.append(a)
                    l.remove(a)


            elif len(x)==k+2:
                if a not in y6:
                    x.append(a)
                    l.remove(a)

        return x

    while l:
        if len(x4)!=c:
            x4=add_remove(x4,y4,y5,y6,k)
        elif len(x5)!=c:
            x5=add_remove(x5,y4,y5,y6,k)
        elif len(x6)!=c:
            x6=add_remove(x6,y4,y5,y6,k)
    return x4,x5,x6


r4,r5,r6=grid_2(r4,r5,r6,3,c1,c2,c3,0)
r4,r5,r6=grid_2(r4,r5,r6,6,c4,c5,c6,3)
r4,r5,r6=grid_2(r4,r5,r6,9,c7,c8,c9,6)
print(r4)
print(r5)
print(r6)

c1,c2,c3=col(r4,r5,r6,c1,c2,c3,0,3)
c4,c5,c6=col(r4,r5,r6,c4,c5,c6,3,6)
c7,c8,c9=col(r4,r5,r6,c7,c8,c9,6,9)

#grid 7,8,9

r7,r8,r9=grid_2(r7,r8,r9,3,c1,c2,c3,0)
r7,r8,r9=grid_2(r7,r8,r9,6,c4,c5,c6,3)
r7,r8,r9=grid_2(r7,r8,r9,9,c7,c8,c9,6)
print(r7)
print(r8)
print(r9)

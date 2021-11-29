c=0
r=10000
for i in range(10,r):
    x=i
    lst=[]
    count=1
    flag=False
    while(x!=0):
        y=int(x%10)
        lst.append(y)
        x=int(x/10)
    rev=0
    for j in range(len(lst)):
        rev=int(rev*10+lst[j])
    sum=0
    sum=i+rev
    temp=sum
    revv=0
    y=0
    while(temp!=0):
        y=int(temp%10)
        revv=int(revv*10+y)
        temp=int(temp/10)
    k=sum

    while sum!=revv:
        x=sum
        lst=[]
        while(x!=0):
            y=int(x%10)
            lst.append(y)
            x=int(x/10)
        rev=0
        for j in range(len(lst)):
            rev=int(rev*10+lst[j])
        sum=0
        sum=k+rev
        temp=sum
        revv=0
        y=0
        while(temp!=0):
            y=int(temp%10)
            revv=int(revv*10+y)
            temp=int(temp/10)
        k=sum
        count+=1
        if count>50:
            flag=True
            break
    if(flag):
        print(i,' is a lycher number ')
        c+=1
str='there are {} Lychrel numbers below {} '
print(str.format(c,r))


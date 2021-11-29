sum=0
temp=0
count=0
for x in range(2,100):
    flag=True
    i=2
    while i<=int(x/2):
        if(x%i==0):
            flag=False
            break
        i+=1
    if(flag):
        temp+=x
        i=2
        while i<=int(temp/2):
            if(temp%i==0):
                flag=False
                break
            i+=1
        if(flag and temp<100):
            sum=temp
    if(temp>100):
        break
print(sum)

count=0
for x in range(2,1000):
    y=x
    flag = True
    i=2
    while i <=int(y/2):
        if(y%i==0):
            flag=False
            break
        i+=1
    k=0
    num=1
    if(flag):
        if(y>=10):
            while(y!=0):
                temp=int(y%10)
                y=int(y/10)
                k+=1
                if(k!=1):
                    num*=10
            y=x
            j=0
            while j!=k :
                temp=int(y%10)
                temp=int(temp*num)
                y=int(y/10)
                temp=temp+y
                i=2
                while i <=int(temp/2):
                    if(temp%i==0):
                        flag=False
                        break
                    i+=1
                if(flag):
                    y=temp
                    j+=1
                else:
                    break
        if(flag):
            print(x)
            count+=1

print('total circular primes are ',count)
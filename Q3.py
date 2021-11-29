
count=0
summ=0
varr=10
while(1):
    flag = True
    j=2
    x=varr
    while j <=int(x/2):
        if(int(x%j)==0):
            flag=False
            break
        j+=1
    if flag:
        waste=str(x)
        k=len(waste)
        lst=[]
        for i in range(k):
            flag = True
            j=2
            while j <=int(x/2):
                if(int(x%j)==0):
                    flag=False
                    break
                j+=1
            lst.append(int(x%10))
            x=int(x/10)
            if not flag :
                break
        newlst=[]
        m=-1
        for y in lst:
            newlst.append(lst[m])
            m=m-1
        i=0
        c=0
        copylst=newlst.copy()
        for h in lst:
            c=0
            for i in range(len(newlst)):
                c=c*10+newlst[i]
            j=2
            while j <=int(c/2):
                if(int(c%j)==0):
                    flag=False
                    break
                j+=1
            if not flag:
                break
            newlst.pop(0)
        for h in lst:
            c=0
            for i in range(len(copylst)):
                c=c*10+copylst[i]
            j=2
            while j <=int(c/2):
                if(int(c%j)==0):
                    flag=False
                    break
                j+=1
            if not flag:
                break
            copylst.pop(-1)
        if flag:
            summ+=varr
            print(varr)
            count+=1
        if count==11:
            break
    varr+=1
print(summ)

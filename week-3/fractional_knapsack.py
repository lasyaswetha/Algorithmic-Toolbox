# Uses python3
import sys

def get_optimal_value(total,l):
    value = 0
    prop=[]
    for i in range(len(l)):
        prop.append([l[i][0]/l[i][1],i])
    prop.sort(reverse=True)
    sum1=0
    i=0
    while(i<=len(l)-1):
        if(total==0):
            break
        if(l[prop[i][1]][1]<=total):
            sum1=sum1+l[prop[i][1]][0]
            total=total-l[prop[i][1]][1]
        else:
            sum1=sum1+(total/l[prop[i][1]][1])*l[prop[i][1]][0]
            total=0
        i+=1
    
    return ('%.4f'%sum1)


t,total=input().split()
t=int(t)
total=int(total)
l=[]
while(t):
    k=list(map(int,input().split()))
    l.append(k)
    t=t-1
print(get_optimal_value(total,l))
    

#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    answer=[]
    while(len(a)!=0):
        maxlen=0
        for i in a:
            if(int(str(i)+str(maxlen))>=int(str(maxlen)+str(i))):
                maxlen=i
        answer.append(maxlen)
        a.remove(maxlen)
        
    return answer

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    s=largest_number(a)
    for i in s:
        print(i,end="")
    

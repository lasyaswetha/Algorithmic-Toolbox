#Uses python3

import sys

def lcs2(a, b):
    dp=[]
    for i in range(len(a)+1):
        l=[]
        for j in range(len(b)+1):
            l.append(0)
        dp.append(l)
    max1=0
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if(a[i-1]==b[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
    return dp[len(a)][len(b)]

if __name__ == '__main__':
    asize=int(input())
    a=list(map(int,input().split()))
    bsize=int(input())
    b=list(map(int,input().split()))

    print(lcs2(a, b))

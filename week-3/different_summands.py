# Uses python3
import sys

def optimal_summands(n):
    summands = []
    if(n==1):
        summands.append(1)
        return summands
    w=n
    for i in range(1,n):
        if(w>2*i):
            summands.append(i)
            w-=i
        else:
            summands.append(w)
            break
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

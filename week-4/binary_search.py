# Uses python3
import sys

def binary_search(a,x):
    low=0
    high=len(a)-1
    while(low<=high):
        mid=(low+high)//2
        if(a[mid]==x):
            return mid
        elif(a[mid]<x):
            low=mid+1
        else:
            high=mid-1
    return -1



if __name__ == '__main__':
    a=list(map(int,input().split()))
    s=a[1:]
    data = list(map(int, input().split()))
    a.sort()
    for x in range(1,data[0]+1):
        # replace with the call to binary_search when implemented
        print(binary_search(s,data[x]), end = ' ')

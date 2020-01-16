# python3
import sys


def compute_min_refills(distance, tank, stops,di1):
    count=0
    variable=0
    for i in range(len(stops)-1):
        if(stops[i+1]-stops[variable]>tank):
            count+=1
            variable=i
        if(stops[i+1]-stops[i]>tank):
            return -1
    return count
            

di1=int(input())
d=int(input())
m=int(input())
stops=list(map(int,input().split()))
stops.insert(0,0)
stops.append(di1)
print(compute_min_refills(di1, d, stops,m))

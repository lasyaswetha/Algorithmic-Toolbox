# Uses python3
import sys

def get_change(m):
    sum=0
    while(m):
        sum=sum+(m//10)
        m=m%10
        sum=sum+(m//5)
        m=m%5
        sum=sum+(m//1)
        m=m%1
    return sum

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

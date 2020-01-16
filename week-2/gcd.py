# Uses python3
import sys

def gcd_naive(a, b):
    if(a==0):
        return b
    else:
        return gcd_naive(b%a,a)



if __name__ == "__main__":
    
    a, b =input().split()
    a=int(a)
    b=int(b)
    print(gcd_naive(a, b))

# Uses python3
import sys
l=[1,1]
for i in range(2,60):
    l.append((l[i-2]+l[i-1])%10)


def get_fibonacci_last_digit_naive(n):
    rem=(n%60)-1
    if(rem==-1):
        return 0
    else:
        return l[rem]

    
n = int(input())
print(get_fibonacci_last_digit_naive(n))


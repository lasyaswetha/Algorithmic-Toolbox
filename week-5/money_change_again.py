# Uses python3
import sys

def get_change(m):
    coins=[1,3,4]
    min_coins=[0]*(m+1)
    for i in range(1,m+1):
        min_coins[i]=10000
        for j in coins:
            if(i>=j):
                tmp=min_coins[i-j]+1
                if(tmp<min_coins[i]):
                    min_coins[i]=tmp
            else:
                break
    return min_coins[m]
if __name__ == '__main__':
    m = int(input())
    print(get_change(m))

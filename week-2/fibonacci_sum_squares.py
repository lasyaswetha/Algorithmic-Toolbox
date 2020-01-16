# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    l=[0, 1, 2, 6, 5, 0, 4, 3, 4, 0, 5, 6, 2, 1, 0, 0, 9, 8, 4, 5, 0, 6, 7, 6, 0, 5, 4, 8, 9, 0]
    return l[n%30]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))

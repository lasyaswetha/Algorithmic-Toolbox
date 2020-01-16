# Uses python3
import sys


def optimal_weight(totalweight, items):
    matrix = []
    for i in range(len(items)+1):
        l = []
        for j in range(totalweight + 1):
            l.append(0)
        matrix.append(l)
    for i in range(1, len(items)+1):
        for j in range(1, totalweight + 1):
            if items[i-1] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(items[i-1] + matrix[i - 1][j - items[i-1]], matrix[i - 1][j])
    return matrix[len(items) ][totalweight]


if __name__ == '__main__':
    w, n = input().split()
    w = int(w)
    n = int(n)
    l = list(map(int, input().split()))
    print(optimal_weight(w, l))

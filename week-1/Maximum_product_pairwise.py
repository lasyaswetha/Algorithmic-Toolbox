# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    numbers.sort(reverse=True)
    max_product=numbers[0]*numbers[1]
    max_product=max_product+0


    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

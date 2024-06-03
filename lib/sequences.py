#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        result = []
    elif length == 1:
        result = [0]
    elif length >= 2:
        result = [0, 1]
        while len(result) < length:
            sum = result[-1] + result[-2]
            result.append(sum)
    print(result)

print_fibonacci(9)


    
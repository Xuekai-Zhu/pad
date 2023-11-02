def solution():
    # Find the least common multiple of 2, 3, and 4 to determine the shortest time
    # after which all three bulbs will be on at the same time
    # The prime factors of 2, 3, and 4 are 2, 3, and 2^2 respectively
    # The least common multiple will be the product of the highest power of each
    # prime factor required to obtain all factors
    lcm = 2**2 * 3

    result = lcm
    return result

print(solution())
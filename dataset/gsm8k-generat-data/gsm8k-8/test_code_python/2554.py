def solution():
    small_apple_cost = 1.5
    medium_apple_cost = 2
    big_apple_cost = 3

    num_small_and_medium = 6 + 6
    num_big = 8

    total_cost = (num_small_and_medium * (small_apple_cost + medium_apple_cost)) + (num_big * big_apple_cost)

    result = total_cost
    return result

print(solution())
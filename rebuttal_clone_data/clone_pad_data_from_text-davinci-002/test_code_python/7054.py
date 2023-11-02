def solution():
    batches_per_day = 3
    baguettes_per_batch = 48
    baguettes_sold_first = 37
    baguettes_sold_second = 52
    baguettes_sold_third = 49
    baguettes_left = baguettes_per_batch - (baguettes_sold_first + baguettes_sold_second + baguettes_sold_third)
    result = baguettes_left

    return result

print(solution())
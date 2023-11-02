def solution():
    pages_left = 158 - 23 - 38 - 61

    # Calculate the number of pages Cora needs to read on Thursday and Friday
    pages_per_day = pages_left / 2
    pages_thursday = pages_per_day / 2

    result = pages_thursday
    return result

print(solution())
def solution():
    total_shoes = 10 * 2 # 10 pairs of shoes, so 20 individual shoes
    polished_shoes = int(total_shoes * 0.45) # 45% of individual shoes, rounded down to a whole number

    # Calculate the number of shoes that still need to be polished
    remaining_shoes = total_shoes - polished_shoes
    result = remaining_shoes
    return result

print(solution())
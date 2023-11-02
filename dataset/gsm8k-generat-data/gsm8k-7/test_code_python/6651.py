def solution():
    total_sweets = 285
    red_sweets = 49
    green_sweets = 59

    # Calculate the number of sweets that are neither red nor green
    neither_sweets = total_sweets - red_sweets - green_sweets
    result = neither_sweets
    return result

print(solution())
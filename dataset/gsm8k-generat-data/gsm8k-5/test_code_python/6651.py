def solution():
    total_sweets = 285  # There are 285 sweets in the bowl
    red_sweets = 49  # 49 of the sweets are red
    green_sweets = 59  # 59 of the sweets are green

    # Calculate the number of sweets that are neither red nor green
    neither_sweets = total_sweets - red_sweets - green_sweets
    result = neither_sweets
    return result

print(solution())
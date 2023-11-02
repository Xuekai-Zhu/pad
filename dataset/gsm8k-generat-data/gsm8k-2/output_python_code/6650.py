def solution():
    """There are 285 sweets in the bowl. If 49 of the sweets are red and 59 of the sweets are green, how many of the sweets are neither red nor green?"""
    total_sweets = 285
    red_sweets = 49
    green_sweets = 59
    neither_sweets = total_sweets - red_sweets - green_sweets
    result = neither_sweets
    return result

print(solution())
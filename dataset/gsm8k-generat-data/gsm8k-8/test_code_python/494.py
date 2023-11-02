def solution():
    # Define the initial sizes of the houses
    small_house = 5200
    large_house = 7300

    # Calculate the current total square footage
    total_sq_ft = small_house + large_house

    # Calculate the expansion of the smaller house
    expansion = (total_sq_ft - 16000) / 2

    result = expansion
    return result

print(solution())
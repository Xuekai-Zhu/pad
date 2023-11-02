def solution():
    # Calculate the total number of bread slices needed
    total_slices = 8 * 2

    # Calculate the number of bread packs needed, rounding up to the nearest whole number
    bread_packs = math.ceil(total_slices / 4)

    result = bread_packs
    return result

print(solution())
def solution():
    # Calculate the total number of bulbs that need to be replaced
    total_bulbs = 2 + 2 + 1 + 4 + 0.5 * (2 + 1 + 4)

    # Calculate the total number of packs needed, rounding up to the nearest whole number
    packs_needed = math.ceil(total_bulbs / 2)

    result = packs_needed
    return result

print(solution())
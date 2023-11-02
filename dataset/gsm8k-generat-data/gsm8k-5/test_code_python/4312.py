def solution():
    # Calculate the total number of light bulbs needed
    total_bulbs = 2 + 1 + 4 + (1/2 * (2+1+4))

    # Calculate the total number of packs of bulbs needed
    packs = total_bulbs / 2

    result = packs
    return result

print(solution())
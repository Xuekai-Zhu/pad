def solution():
    # Calculate the total number of light bulbs needed
    total_bulbs = 2 + 1 + 1 + 4  # 2 in bedroom, 1 in bathroom and kitchen each, 4 in basement
    total_bulbs += total_bulbs / 2  # add 1/2 of total for garage
    packs_needed = total_bulbs / 2  # each pack contains 2 bulbs
    result = packs_needed
    return result

print(solution())
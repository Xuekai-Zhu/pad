def solution():
    # Calculate the total number of rolls needed for 4 weeks
    rolls_needed = 6 * 7 * 4

    # Calculate the number of packs of toilet paper dozens needed
    rolls_per_dozen = 12
    packs_needed = rolls_needed / rolls_per_dozen

    # Round up to the nearest whole number of packs
    packs_needed = int(packs_needed) + (packs_needed % 1 > 0)

    result = packs_needed
    return result

print(solution())
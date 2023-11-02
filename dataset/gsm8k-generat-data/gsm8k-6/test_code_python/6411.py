def solution():
    # Calculate the number of each material needed for one earring
    magnets_per_earring = 2
    buttons_per_earring = (1/2) * magnets_per_earring
    gemstones_per_earring = 3 * buttons_per_earring

    # Calculate the total number of gemstones needed for 4 sets of earrings
    gemstones_total = 4 * 2 * gemstones_per_earring  # 4 sets of earrings with 2 earrings per set

    result = gemstones_total
    return result

print(solution())
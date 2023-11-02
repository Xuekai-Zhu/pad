def solution():
    # Calculate the total volume of the raised beds
    bed_volume = 2 * 8 * 4 * 1  # two beds, each 8 feet long, 4 feet wide, and 1 foot high

    # Calculate the number of bags of soil needed (rounded up to the nearest integer)
    bags_needed = math.ceil(bed_volume / 4)  # each bag has 4 cubic feet of soil

    result = bags_needed
    return result

print(solution())
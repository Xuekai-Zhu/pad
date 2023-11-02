def solution():
    # Calculate the number of 12-sided dice Mark has
    mark_12_sided = 0.6 * 10

    # Calculate the number of 12-sided dice James has
    james_12_sided = 0.75 * 8

    # Calculate the total number of 12-sided dice the boys have
    total_12_sided = mark_12_sided + james_12_sided

    # Calculate the number of additional dice needed
    additional_dice = 14 - total_12_sided

    result = additional_dice
    return result

print(solution())
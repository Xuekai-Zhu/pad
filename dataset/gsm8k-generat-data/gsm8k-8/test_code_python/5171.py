def solution():
    # Calculate the volume of one raised bed
    bed_volume = 8 * 4 * 1

    # Calculate the total volume of both raised beds
    total_volume = bed_volume * 2

    # Calculate the number of bags of soil needed
    bags_needed = total_volume / 4

    result = bags_needed
    return result

print(solution())
def solution():
    # Calculate the total number of beads
    total_beads = 23 + 16

    # Calculate the number of beads in each part before removing some
    beads_per_part = total_beads // 3

    # Calculate the number of beads in each part after doubling the remaining beads
    beads_per_part *= 2

    # Calculate the number of beads removed from each part
    beads_removed = (23 % 3 + 16 % 3) * 2

    result = beads_removed // 3
    return result

print(solution())
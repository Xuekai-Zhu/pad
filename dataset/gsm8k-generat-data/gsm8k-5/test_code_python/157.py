def solution():
    total_beads = 23 + 16  # The total number of beads is the sum of blue and yellow beads
    parts = 3  # The total number of equal parts

    # Divide the total number of beads into equal parts
    beads_per_part = total_beads / parts

    # Calculate the number of beads doubled in each part
    doubled_beads = 6
    doubled_beads_per_part = doubled_beads - (beads_per_part / 2)

    # Calculate the number of beads removed from each part
    removed_beads_per_part = beads_per_part / 2 - doubled_beads_per_part
    result = removed_beads_per_part
    return result

print(solution())
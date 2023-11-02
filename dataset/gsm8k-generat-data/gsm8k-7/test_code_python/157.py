def solution():
    num_blue_beads = 23
    num_yellow_beads = 16
    total_beads = num_blue_beads + num_yellow_beads
    num_parts = 3

    # Calculate the number of beads in each part before removal
    beads_per_part_before_removal = total_beads / num_parts

    # Calculate the number of beads in each part after doubling and rearranging
    beads_per_part_after_rearrange = 6

    # Calculate the number of beads removed from each part
    beads_removed_per_part = (beads_per_part_before_removal - beads_per_part_after_rearrange) / 2
    result = beads_removed_per_part
    return result

print(solution())
def solution():
    # Calculate the number of beads in each pattern
    green_beads = 3
    purple_beads = 5
    red_beads = 2 * green_beads
    total_beads_per_pattern = green_beads + purple_beads + red_beads

    # Calculate the number of beads needed for one bracelet
    total_beads_per_bracelet = total_beads_per_pattern * 3

    # Calculate the number of beads needed for 10 necklaces
    total_beads_per_necklace = total_beads_per_pattern * 5
    total_beads_for_10_necklaces = total_beads_per_necklace * 10

    # Calculate the total number of beads needed
    total_beads = total_beads_per_bracelet + total_beads_for_10_necklaces
    result = total_beads
    return result

print(solution())
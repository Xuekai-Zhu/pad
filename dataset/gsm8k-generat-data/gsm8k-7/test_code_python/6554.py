def solution():
    total_beads = 40
    blue_beads = 5
    red_beads = 2 * blue_beads
    white_beads = blue_beads + red_beads

    # Calculate the total number of non-silver beads used
    non_silver_beads = blue_beads + red_beads + white_beads

    # Calculate the number of silver beads used
    silver_beads = total_beads - non_silver_beads
    result = silver_beads
    return result

print(solution())
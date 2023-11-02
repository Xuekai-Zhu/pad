def solution():
    num_purple_beads = 7
    num_blue_beads = 2 * num_purple_beads
    num_green_beads = num_blue_beads + 11

    # Calculate the total number of beads in the necklace
    total_beads = num_purple_beads + num_blue_beads + num_green_beads
    result = total_beads
    return result

print(solution())
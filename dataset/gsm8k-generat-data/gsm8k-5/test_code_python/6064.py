def solution():
    purple_beads = 7
    blue_beads = 2 * purple_beads  # Blue beads are twice as many as purple beads
    green_beads = blue_beads + 11  # Green beads are 11 more than blue beads

    # Calculate the total number of beads in the necklace
    total_beads = purple_beads + blue_beads + green_beads
    result = total_beads
    return result

print(solution())
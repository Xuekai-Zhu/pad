def solution():
    # Calculate the number of beads in one repetition of the pattern
    green_beads = 3
    purple_beads = 5
    red_beads = 2 * green_beads
    total_beads_in_pattern = green_beads + purple_beads + red_beads

    # Calculate the number of beads needed for one bracelet and ten necklaces
    beads_per_bracelet = 3 * total_beads_in_pattern
    beads_per_necklace = 5 * total_beads_in_pattern
    total_beads = beads_per_bracelet + 10 * beads_per_necklace

    result = total_beads
    return result

print(solution())
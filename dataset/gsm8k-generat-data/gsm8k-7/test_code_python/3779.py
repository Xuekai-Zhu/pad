def solution():
    green_beads = 3
    purple_beads = 5
    red_beads = 2 * green_beads

    pattern_length = green_beads + purple_beads + red_beads
    bracelets_per_pattern = 1
    necklaces_per_pattern = 5
    patterns_per_bracelet = 3
    patterns_per_necklace = 10

    # Calculate the total number of beads needed for one pattern
    beads_per_pattern = pattern_length * (bracelets_per_pattern + necklaces_per_pattern)

    # Calculate the total number of beads needed for all patterns for one bracelet
    beads_per_bracelet = beads_per_pattern * patterns_per_bracelet

    # Calculate the total number of beads needed for all patterns for ten necklaces
    beads_per_necklaces = beads_per_pattern * patterns_per_necklace * 10

    # Calculate the total number of beads needed for one bracelet and ten necklaces
    total_beads = beads_per_bracelet + beads_per_necklaces
    result = total_beads
    return result

print(solution())
def solution():
    green_beads = 3  # Each pattern has 3 green beads
    purple_beads = 5  # Each pattern has 5 purple beads
    red_beads = 2 * green_beads  # Each pattern has twice as many red beads as green beads
    pattern_length = green_beads + purple_beads + red_beads  # Total number of beads in each pattern
    bracelets = 1  # Susan wants to make 1 bracelet
    necklaces = 10  # Susan wants to make 10 necklaces

    # Calculate the total number of beads needed for bracelets and necklaces
    total_beads = (bracelets * pattern_length * 3) + (necklaces * pattern_length * 5)

    result = total_beads
    return result

print(solution())
def solution():
    """Michelle uses 40 beads in making a necklace. She uses 5 blue beads and 2 times as many red beads as blue beads. Then she uses the same number of white beads as the blue and red beads combined. If the rest of the beads she uses are silver, how many silver beads does she use?"""
    total_beads = 40
    blue_beads = 5
    red_beads = 2 * blue_beads
    white_beads = blue_beads + red_beads
    used_beads = blue_beads + red_beads + white_beads
    silver_beads = total_beads - used_beads
    result = silver_beads
    return result

print(solution())
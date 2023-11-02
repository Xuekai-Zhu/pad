def solution():
    """All of the beads in Sue's necklace are either purple, blue, or green. If Sue has 7 purple beads, twice as many blue beads as purple beads, and 11 more green beads than blue beads, how many beads are in the necklace?"""
    purple_beads = 7
    blue_beads = 2 * purple_beads
    green_beads = blue_beads + 11
    total_beads = purple_beads + blue_beads + green_beads
    result = total_beads
    return result

print(solution())
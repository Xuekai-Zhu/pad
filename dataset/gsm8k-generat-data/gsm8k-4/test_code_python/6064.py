def solution():
    """All of the beads in Sue's necklace are either purple, blue, or green. If Sue has 7 purple beads, twice as many blue beads as purple beads, and 11 more green beads than blue beads, how many beads are in the necklace?"""
    # Define the number of purple beads
    purple_beads = 7

    # Calculate the number of blue beads
    blue_beads = purple_beads * 2

    # Calculate the number of green beads
    green_beads = blue_beads + 11

    # Calculate the total number of beads
    total_beads = purple_beads + blue_beads + green_beads

    # return the result
    result = total_beads
    return result

print(solution())
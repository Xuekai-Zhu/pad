def solution():
    """All of the beads in Sue's necklace are either purple, blue, or green. If Sue has 7 purple beads, twice as many blue beads as purple beads, and 11 more green beads than blue beads, how many beads are in the necklace?"""
    # Define the number of purple beads
    purple_beads = 7

    # Define the number of blue beads (twice the number of purple beads)
    blue_beads = 2 * purple_beads

    # Define the number of green beads (11 more than the number of blue beads)
    green_beads = blue_beads + 11

    # Calculate the total number of beads
    total_beads = purple_beads + blue_beads + green_beads

    # Display the total number of beads in the necklace
    result = total_beads
    return result

print(solution())
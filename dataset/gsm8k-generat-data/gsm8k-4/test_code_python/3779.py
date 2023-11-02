def solution():
    """Susan is making jewelry with a repeating pattern that has 3 green beads, 5 purple beads, and twice as many red beads as green beads. If the pattern repeats three times per bracelet and 5 times per necklace, how many beads does she need to make 1 bracelets and 10 necklaces?"""
    # Define the number of beads for each color in the pattern
    green_beads = 3
    purple_beads = 5
    red_beads = 2 * green_beads

    # Define the number of times the pattern repeats for each bracelet and necklace
    bracelet_repeats = 3
    necklace_repeats = 5

    # Calculate the total number of beads needed for one bracelet
    bracelet_beads = (green_beads + purple_beads + red_beads) * bracelet_repeats

    # Calculate the total number of beads needed for ten necklaces
    necklace_beads = (green_beads + purple_beads + red_beads) * necklace_repeats * 10

    # Calculate the total number of beads needed for both the bracelet and the necklaces
    total_beads = bracelet_beads + necklace_beads

    # return the result
    result = total_beads
    return result

print(solution())
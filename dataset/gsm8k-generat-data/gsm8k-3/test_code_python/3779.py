def solution():
    """Susan is making jewelry with a repeating pattern that has 3 green beads, 5 purple beads, and twice as many red beads as green beads. If the pattern repeats three times per bracelet and 5 times per necklace, how many beads does she need to make 1 bracelets and 10 necklaces?"""
    # Define the number of beads in the repeating pattern
    green_beads = 3
    purple_beads = 5
    red_beads = green_beads * 2

    # Define the number of repeats per bracelet and necklace
    repeats_per_bracelet = 3
    repeats_per_necklace = 5

    # Calculate the total number of beads needed for one bracelet
    beads_per_bracelet = (green_beads + purple_beads + red_beads) * repeats_per_bracelet

    # Calculate the total number of beads needed for 10 necklaces
    beads_per_necklace = (green_beads + purple_beads + red_beads) * repeats_per_necklace
    beads_per_10_necklaces = beads_per_necklace * 10

    # Calculate the total number of beads needed
    total_beads = beads_per_bracelet + beads_per_10_necklaces

    # Display the total number of beads
    result = total_beads
    return result

print(solution())
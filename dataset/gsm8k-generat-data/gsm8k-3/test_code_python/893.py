def solution():
    """Kylie makes 10 beaded necklaces on Monday and 2 beaded necklaces on Tuesday. Then Kylie makes 5 beaded bracelets and 7 beaded earrings on Wednesday. 20 beads are needed to make one beaded necklace. 10 beads are needed to make one beaded bracelet. 5 beads are needed to make one beaded earring. How many beads does Kylie use in total to make her jewelry?"""
    # Define the number of beads needed for each type of jewelry
    NECKLACE_BEADS = 20
    BRACELET_BEADS = 10
    EARRING_BEADS = 5

    # Calculate the total number of beads used for the necklaces
    necklace_beads = (10 + 2) * NECKLACE_BEADS

    # Calculate the total number of beads used for the bracelets
    bracelet_beads = 5 * BRACELET_BEADS

    # Calculate the total number of beads used for the earrings
    earring_beads = 7 * EARRING_BEADS

    # Calculate the total number of beads used for all the jewelry
    total_beads = necklace_beads + bracelet_beads + earring_beads

    # Display the total number of beads used
    result = total_beads
    return result

print(solution())
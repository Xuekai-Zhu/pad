def solution():
    """Kylie makes 10 beaded necklaces on Monday and 2 beaded necklaces on Tuesday. Then Kylie makes 5 beaded bracelets and 7 beaded earrings on Wednesday. 20 beads are needed to make one beaded necklace. 10 beads are needed to make one beaded bracelet. 5 beads are needed to make one beaded earring. How many beads does Kylie use in total to make her jewelry?"""
    # Define the number of beaded necklaces and the number of required beads per necklace
    monday_necklaces = 10
    tuesday_necklaces = 2
    necklace_beads = 20

    # Define the number of beaded bracelets and the number of required beads per bracelet
    wednesday_bracelets = 5
    bracelet_beads = 10

    # Define the number of beaded earrings and the number of required beads per earring
    wednesday_earrings = 7
    earring_beads = 5

    # Calculate the total number of beads used for each type of jewelry
    total_necklace_beads = (monday_necklaces + tuesday_necklaces) * necklace_beads
    total_bracelet_beads = wednesday_bracelets * bracelet_beads
    total_earring_beads = wednesday_earrings * earring_beads

    # Calculate the total number of beads used for all the jewelry
    total_beads_used = total_necklace_beads + total_bracelet_beads + total_earring_beads

    # return the result
    result = total_beads_used
    return result

print(solution())
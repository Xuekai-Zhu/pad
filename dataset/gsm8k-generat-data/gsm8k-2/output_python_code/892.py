def solution():
    """Kylie makes 10 beaded necklaces on Monday and 2 beaded necklaces on Tuesday. Then Kylie makes 5 beaded bracelets and 7 beaded earrings on Wednesday. 20 beads are needed to make one beaded necklace. 10 beads are needed to make one beaded bracelet. 5 beads are needed to make one beaded earring. How many beads does Kylie use in total to make her jewelry?"""
    monday_necklaces = 10
    tuesday_necklaces = 2
    wednesday_bracelets = 5
    wednesday_earrings = 7
    necklace_beads = 20
    bracelet_beads = 10
    earring_beads = 5
    total_beads = (monday_necklaces + tuesday_necklaces) * necklace_beads + wednesday_bracelets * bracelet_beads + wednesday_earrings * earring_beads
    result = total_beads
    return result

print(solution())
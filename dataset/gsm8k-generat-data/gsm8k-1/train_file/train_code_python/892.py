def solution():
    """Kylie makes 10 beaded necklaces on Monday and 2 beaded necklaces on Tuesday. Then Kylie makes 5 beaded bracelets and 7 beaded earrings on Wednesday. 20 beads are needed to make one beaded necklace. 10 beads are needed to make one beaded bracelet. 5 beads are needed to make one beaded earring. How many beads does Kylie use in total to make her jewelry?"""
    necklaces_monday = 10
    necklaces_tuesday = 2
    bracelets = 5
    earrings = 7
    beads_per_necklace = 20
    beads_per_bracelet = 10
    beads_per_earring = 5
    total_beads = (necklaces_monday + necklaces_tuesday) * beads_per_necklace + bracelets * beads_per_bracelet + earrings * beads_per_earring
    result = total_beads
    return result

print(solution())
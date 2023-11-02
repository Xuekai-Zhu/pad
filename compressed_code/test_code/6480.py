def solution():
    
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
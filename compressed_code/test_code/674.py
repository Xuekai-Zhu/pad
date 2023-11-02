def solution():
    
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
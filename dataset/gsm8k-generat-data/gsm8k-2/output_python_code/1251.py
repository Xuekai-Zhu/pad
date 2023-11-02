def solution():
    """Marnie makes bead bracelets. She bought 5 bags of 50 beads and 2 bags of 100 beads. If 50 beads are used to make one bracelet, how many bracelets will Marnie be able to make out of the beads she bought?"""
    total_beads = 5 * 50 + 2 * 100
    beads_per_bracelet = 50
    total_bracelets = total_beads // beads_per_bracelet
    result = total_bracelets
    return result

print(solution())
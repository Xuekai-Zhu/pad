def solution():
    """Marnie makes bead bracelets. She bought 5 bags of 50 beads and 2 bags of 100 beads. If 50 beads are used to make one bracelet, how many bracelets will Marnie be able to make out of the beads she bought?"""
    bags_of_50 = 5
    bags_of_100 = 2
    beads_per_bracelet = 50
    total_beads = (bags_of_50 * 50) + (bags_of_100 * 100)
    bracelets_made = total_beads // beads_per_bracelet
    result = bracelets_made
    return result

print(solution())
def solution():
    
    bags_of_50 = 5
    bags_of_100 = 2
    beads_per_bracelet = 50
    total_beads = (bags_of_50 * 50) + (bags_of_100 * 100)
    bracelets_made = total_beads // beads_per_bracelet
    result = bracelets_made
    return result

print(solution())
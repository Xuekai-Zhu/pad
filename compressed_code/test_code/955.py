def solution():
    
    total_beads = 5 * 50 + 2 * 100
    beads_per_bracelet = 50
    total_bracelets = total_beads // beads_per_bracelet
    result = total_bracelets
    return result

print(solution())
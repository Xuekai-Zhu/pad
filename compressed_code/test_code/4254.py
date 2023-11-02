def solution():
    
    purple_beads = 50 * 20
    blue_beads = 40 * 18
    gold_beads = 80
    total_beads = purple_beads + blue_beads + gold_beads
    bead_cost = total_beads / 10
    result = round(bead_cost, 2)
    return result

print(solution())
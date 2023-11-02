def solution():
    """Carly is making a beaded corset. She's going to add 50 rows of purple beads with 20 beads per row, 40 rows of blue beads with 18 beads per row, and 80 gold beads. If beads cost $1 per 10 beads, how much do all the beads she bought cost?"""
    purple_beads = 50 * 20
    blue_beads = 40 * 18
    gold_beads = 80
    total_beads = purple_beads + blue_beads + gold_beads
    bead_cost = total_beads / 10
    result = round(bead_cost, 2)
    return result

print(solution())
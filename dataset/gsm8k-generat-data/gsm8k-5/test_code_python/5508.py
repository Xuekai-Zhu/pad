def solution():
    purple_beads = 50 * 20  # 50 rows of purple beads with 20 beads per row
    blue_beads = 40 * 18  # 40 rows of blue beads with 18 beads per row
    gold_beads = 80  # 80 gold beads

    total_beads = purple_beads + blue_beads + gold_beads  # Total number of beads used
    cost_per_bead = 0.1  # Cost per bead is $1 per 10 beads
    total_cost = total_beads * cost_per_bead  # Total cost of all beads

    result = total_cost
    return result

print(solution())
def solution():
    purple_beads_per_row = 20
    num_purple_rows = 50
    blue_beads_per_row = 18
    num_blue_rows = 40
    num_gold_beads = 80

    bead_cost_per_ten = 1

    # Calculate the total number of purple beads
    total_purple_beads = purple_beads_per_row * num_purple_rows

    # Calculate the total number of blue beads
    total_blue_beads = blue_beads_per_row * num_blue_rows

    # Calculate the total number of all beads
    total_beads = total_purple_beads + total_blue_beads + num_gold_beads

    # Calculate the total cost of all beads
    total_cost = (total_beads / 10) * bead_cost_per_ten
    result = total_cost
    return result

print(solution())
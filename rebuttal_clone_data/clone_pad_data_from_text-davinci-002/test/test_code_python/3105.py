def solution():
    number_of_purple_beads = 50
    beads_per_row_of_purple = 20
    number_of_blue_beads = 40
    beads_per_row_of_blue = 18
    number_of_gold_beads = 80
    cost_of_purple_beads = (number_of_purple_beads * beads_per_row_of_purple) / 10
    cost_of_blue_beads = (number_of_blue_beads * beads_per_row_of_blue) / 10
    cost_of_gold_beads = number_of_gold_beads / 10
    total_cost = cost_of_purple_beads + cost_of_blue_beads + cost_of_gold_beads
    result = total_cost
    
    return result

print(solution())
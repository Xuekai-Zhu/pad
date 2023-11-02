def solution():
    # Plants for each planter
    palm_fern = 1
    creeping_jennies = 4
    geraniums = 4

    # Cost of each plant
    cost_palm_fern = 15
    cost_creeping_jennies = 4
    cost_geraniums = 3.5

    # Number of pots
    number_of_pots = 4

    # Total cost for each pot
    cost_per_pot = (palm_fern * cost_palm_fern) + (creeping_jennies * cost_creeping_jennies) + (geraniums * cost_geraniums)

    # Total cost for all pots
    total_cost = cost_per_pot * number_of_pots
    result = total_cost
    return result

print(solution())
def solution():
    cost_per_cabinet_knob = 2.50  # Each cabinet knob costs $2.50
    cost_per_drawer_pull = 4.00  # Each drawer pull costs $4.00
    num_cabinet_knobs = 18  # Amanda is replacing 18 cabinet knobs
    num_drawer_pulls = 8  # Amanda is replacing 8 drawer pulls

    # Calculate the total cost of the cabinet knobs and drawer pulls
    total_cost = (cost_per_cabinet_knob * num_cabinet_knobs) + (cost_per_drawer_pull * num_drawer_pulls)
    result = total_cost
    return result

print(solution())
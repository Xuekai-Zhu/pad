def solution():
    # Calculate the total cost for Jason
    stove_cost = 1200  # cost for buying a new stove
    wall_damage_cost = stove_cost / 6  # cost for fixing the wall damage
    total_cost = stove_cost + wall_damage_cost  # total cost for Jason
    result = total_cost
    return result

print(solution())
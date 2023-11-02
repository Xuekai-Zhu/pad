def solution():
    replacement_cost = 1200  # Cost of buying a replacement stove
    wall_damage_cost = replacement_cost / 6  # Cost of fixing the wall damage

    # Total cost of replacing the stove and fixing the wall damage
    total_cost = replacement_cost + wall_damage_cost
    result = total_cost
    return result

print(solution())
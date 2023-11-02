def solution():
    
    num_robes_needed = 30
    num_robes_owned = 12
    num_robes_to_buy = num_robes_needed - num_robes_owned
    robe_cost = 2
    total_cost = num_robes_to_buy * robe_cost
    result = total_cost
    return result

print(solution())
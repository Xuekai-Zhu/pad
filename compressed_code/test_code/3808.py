def solution():
    
    fish_weight = 540
    crate_weight = 30
    num_crates = fish_weight // crate_weight + (1 if fish_weight % crate_weight != 0 else 0)
    shipping_cost = 1.5
    total_cost = num_crates * shipping_cost
    result = total_cost
    return result

print(solution())
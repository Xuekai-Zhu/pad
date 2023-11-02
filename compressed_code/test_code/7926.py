def solution():
    
    max_weight_per_crate = 20  
    num_crates = 3
    cost_of_crates = 330  
    price_per_kg = 6  
    rotten_tomatoes_weight = 3  

    max_total_weight = max_weight_per_crate * num_crates
    total_weight = max_total_weight - rotten_tomatoes_weight
    total_profit = (total_weight * price_per_kg) - cost_of_crates

    result = total_profit
    return result

print(solution())
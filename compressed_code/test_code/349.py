def solution():
    
    initial_weight = 156
    growth_weight = 36
    current_weight = initial_weight + growth_weight
    monthly_loss = current_weight / 8
    total_loss = 3 * monthly_loss
    new_weight = current_weight - total_loss
    weight_difference = initial_weight - new_weight
    result = weight_difference
    return result

print(solution())
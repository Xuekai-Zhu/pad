def solution():
    
    starting_weight = 220
    weight_loss_percent = 10
    weight_loss = starting_weight * (weight_loss_percent / 100)
    current_weight = starting_weight - weight_loss + 2
    result = current_weight
    return result

print(solution())
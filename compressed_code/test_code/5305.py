def solution():
    
    starting_weight = 250
    monthly_loss = 8
    total_loss = monthly_loss * 12
    final_weight = starting_weight - total_loss
    result = final_weight
    return result

print(solution())
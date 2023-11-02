def solution():
    
    starting_weight = 250
    first_month_loss = 3 * 4
    remaining_loss = 2 * 8
    current_weight = starting_weight - first_month_loss - remaining_loss
    result = current_weight
    return result

print(solution())
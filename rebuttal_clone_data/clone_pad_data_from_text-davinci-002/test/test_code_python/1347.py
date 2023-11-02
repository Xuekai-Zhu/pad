def solution():
 
    Robbie_weight = 100
    Patty_start_weight = Robbie_weight * 4.5
    Patty_loss = 235
    Patty_current_weight = Patty_start_weight - Patty_loss
    weight_difference = Patty_current_weight - Robbie_weight
    result = weight_difference
    return result

print(solution())
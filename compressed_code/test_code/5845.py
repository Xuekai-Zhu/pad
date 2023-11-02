def solution():
    
    initial_weight = 97
    weight_loss_per_month = 3
    months_until_fight = 4
    final_weight = initial_weight - (weight_loss_per_month * months_until_fight)
    result = final_weight
    return result

print(solution())
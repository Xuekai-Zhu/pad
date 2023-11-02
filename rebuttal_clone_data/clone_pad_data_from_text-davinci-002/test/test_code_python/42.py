def solution():
    
    initial_weight = 97
    weight_loss_per_month = 3
    months_until_fight = 4
    total_weight_loss = weight_loss_per_month * months_until_fight
    weight_on_fight_day = initial_weight - total_weight_loss
    result = weight_on_fight_day
    return result

print(solution())
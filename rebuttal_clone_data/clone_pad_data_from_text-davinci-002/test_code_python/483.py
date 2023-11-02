def solution():
    initial_weight = 156
    growth_inches = 3
    growth_pounds = 36
    months_exercising = 3
    weight_loss_rate = initial_weight / 8
    current_weight = initial_weight + (growth_inches * growth_pounds) - (months_exercising * weight_loss_rate)
    weight_difference = initial_weight - current_weight
    
    return weight_difference

print(solution())
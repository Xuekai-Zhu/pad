def solution():
    initial_weight = 250
    weight_loss_per_month = 8
    months_in_year = 12
    total_weight_loss = weight_loss_per_month * months_in_year
    final_weight = initial_weight - total_weight_loss
    result = final_weight
    return result

print(solution())
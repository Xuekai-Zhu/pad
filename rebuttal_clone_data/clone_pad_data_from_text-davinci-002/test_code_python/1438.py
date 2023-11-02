def solution():
    initial_weight = 80
    weight_lost_per_day = initial_weight / 2
    days = 4
    final_weight = initial_weight - (weight_lost_per_day * days)
    result = final_weight
    return result

print(solution())
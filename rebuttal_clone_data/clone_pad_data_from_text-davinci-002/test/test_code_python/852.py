def solution():
    initial_weight = 50000
    weight_delivered_1 = initial_weight * 0.1
    weight_leftover = initial_weight - weight_delivered_1
    weight_delivered_2 = weight_leftover * 0.2
    final_weight = weight_leftover - weight_delivered_2
    result = final_weight
    return result

print(solution())
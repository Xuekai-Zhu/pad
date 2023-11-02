def solution():
    starting_weight = 220
    weight_loss = starting_weight * 0.1
    weight_gain = 2
    final_weight = starting_weight - weight_loss + weight_gain
    result = final_weight
    return result

print(solution())
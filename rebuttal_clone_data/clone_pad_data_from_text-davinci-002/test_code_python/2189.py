def solution():
    tom_weight = 150
    weight_vest = tom_weight / 2
    weight_in_each_hand = tom_weight * 1.5
    total_weight = weight_vest + (weight_in_each_hand * 2)
    result = total_weight
    return result

print(solution())
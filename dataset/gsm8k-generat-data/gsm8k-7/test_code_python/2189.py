def solution():
    weight = 150
    weight_in_each_hand = 1.5 * weight
    weight_vest = 0.5 * weight

    # Calculate the total weight in each hand
    total_weight_in_hands = weight_in_each_hand * 2

    # Calculate the total weight that Tom was moving
    total_weight = total_weight_in_hands + weight_vest
    result = total_weight
    return result

print(solution())
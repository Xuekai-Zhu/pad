def solution():
    starting_weight = 220  # John weighs 220 pounds when he starts exercising
    weight_loss = starting_weight * 0.1  # John loses 10% of his body weight
    current_weight = starting_weight - weight_loss  # John's current weight after losing weight
    current_weight += 2  # John gains back 2 pounds
    result = current_weight
    return result

print(solution())
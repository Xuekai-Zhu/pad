def solution():
    # Define John's starting weight
    starting_weight = 220

    # Calculate the amount of weight he loses
    weight_lost = 0.1 * starting_weight

    # Calculate his weight after losing weight
    weight_after_loss = starting_weight - weight_lost

    # Calculate his weight after gaining back 2 pounds
    final_weight = weight_after_loss + 2

    result = final_weight
    return result

print(solution())
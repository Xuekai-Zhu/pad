def solution():
    start_weight = 220
    weight_loss_percent = 0.1
    weight_gain = 2

    # Calculate the amount of weight John loses
    weight_loss = start_weight * weight_loss_percent

    # Calculate John's weight after losing weight
    weight_after_loss = start_weight - weight_loss

    # Calculate John's weight after gaining some weight back
    weight_at_end = weight_after_loss + weight_gain
    result = weight_at_end
    return result

print(solution())
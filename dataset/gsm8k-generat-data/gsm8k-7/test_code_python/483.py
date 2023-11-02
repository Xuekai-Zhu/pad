def solution():
    starting_weight = 156
    height_gain = 3
    weight_gain = 36
    weight_loss_per_month = starting_weight / 8 / 3

    # Calculate Andy's new weight after height and weight gain
    new_weight = starting_weight + weight_gain

    # Calculate Andy's weight after 3 months of weight loss
    for i in range(3):
        new_weight -= weight_loss_per_month

    # Calculate the difference between Andy's starting weight and current weight
    weight_difference = starting_weight - new_weight
    result = weight_difference
    return result

print(solution())
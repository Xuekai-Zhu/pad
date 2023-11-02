def solution():
    blue_weight = 2
    green_weight = 3
    num_blue_weights = 4
    num_green_weights = 5
    bar_weight = 2

    # Calculate the total weight of all blue weights
    total_blue_weight = blue_weight * num_blue_weights

    # Calculate the total weight of all green weights
    total_green_weight = green_weight * num_green_weights

    # Calculate the total weight of Harry's custom creation
    total_weight = total_blue_weight + total_green_weight + bar_weight
    result = total_weight
    return result

print(solution())
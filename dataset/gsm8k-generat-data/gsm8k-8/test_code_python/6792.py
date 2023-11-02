def solution():
    # Calculate weight gain for each puppy
    lab_weight_gain = 40 * 0.25
    dachshund_weight_gain = 12 * 0.25

    # Calculate final weights for each puppy
    lab_final_weight = 40 + lab_weight_gain
    dachshund_final_weight = 12 + dachshund_weight_gain

    # Calculate the difference in their weights
    weight_diff = lab_final_weight - dachshund_final_weight
    result = weight_diff
    return result

print(solution())
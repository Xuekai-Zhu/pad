def solution():
    labrador_weight = 40
    dachshund_weight = 12
    weight_gain_percentage = 0.25  # 25% weight gain

    # Calculate the weight of each dog at the end of the year
    labrador_end_weight = labrador_weight + (labrador_weight * weight_gain_percentage)
    dachshund_end_weight = dachshund_weight + (dachshund_weight * weight_gain_percentage)

    # Calculate the difference in weight between the two dogs at the end of the year
    weight_difference = labrador_end_weight - dachshund_end_weight
    result = weight_difference
    return result

print(solution())
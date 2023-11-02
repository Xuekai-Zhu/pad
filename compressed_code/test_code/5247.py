def solution():
    
    labrador_weight = 40
    dachshund_weight = 12

    labrador_gain = labrador_weight * 0.25
    dachshund_gain = dachshund_weight * 0.25

    labrador_weight += labrador_gain
    dachshund_weight += dachshund_gain

    weight_difference = labrador_weight - dachshund_weight
    result = weight_difference
    return result

print(solution())
def solution():
    
    num_plates = 10
    plate_weight = 30
    weight_increase = 0.2
    lowered_weight = (1 + weight_increase) * plate_weight
    total_weight_lowered = num_plates * lowered_weight
    result = total_weight_lowered
    return result

print(solution())
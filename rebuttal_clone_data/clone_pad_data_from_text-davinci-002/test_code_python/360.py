def solution():
    oil_to_peanut_ratio = 2/8
    total_weight = 20
    peanut_weight = total_weight / (1 + oil_to_peanut_ratio)
    oil_weight = total_weight - peanut_weight
    result = oil_weight
    
    return result

print(solution())
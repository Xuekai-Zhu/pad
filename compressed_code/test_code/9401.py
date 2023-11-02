def solution():
    
    bowl_size = 150
    oil_ratio = 2/3
    vinegar_ratio = 1/3
    oil_weight = 5
    vinegar_weight = 4
    oil_amount = bowl_size * oil_ratio
    vinegar_amount = bowl_size * vinegar_ratio
    total_weight = (oil_amount * oil_weight) + (vinegar_amount * vinegar_weight)
    result = total_weight
    return result

print(solution())
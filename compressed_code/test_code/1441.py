def solution():
    
    weight_per_bushel = 56
    weight_per_corn = 0.5
    total_weight = weight_per_bushel * 2
    total_corn = total_weight / weight_per_corn
    result = total_corn
    return result

print(solution())
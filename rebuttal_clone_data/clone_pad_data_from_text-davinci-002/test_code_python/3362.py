def solution():
    max_weight_american = 5
    max_weight_european = max_weight_american * 2
    number_american = 90 / 2
    number_european = 90 - number_american
    total_weight = (max_weight_american * number_american) + (max_weight_european * number_european)
    result = total_weight
    
    return result

print(solution())
def solution():
    
    max_load = 700
    adult_weight = 80
    num_adults = 8
    total_adult_weight = adult_weight * num_adults
    max_load_exceeded = max_load - total_adult_weight
    result = max_load_exceeded
    return result

print(solution())
def solution():
    
    american_swallow_weight = 5
    european_swallow_weight = american_swallow_weight * 2
    num_american_swallows = 2/3 * 90
    num_european_swallows = 1/3 * 90
    total_weight = (num_american_swallows * american_swallow_weight) + (num_european_swallows * european_swallow_weight)
    result = total_weight
    return result

print(solution())
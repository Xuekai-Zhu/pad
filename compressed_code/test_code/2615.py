def solution():
    
    american_swallow_weight = 5
    european_swallow_weight = 2 * american_swallow_weight
    total_swallows = 90
    american_swallows = total_swallows * 2 / 3
    european_swallows = total_swallows * 1 / 3
    total_weight = american_swallow_weight * american_swallows + european_swallow_weight * european_swallows
    result = total_weight
    return result

print(solution())
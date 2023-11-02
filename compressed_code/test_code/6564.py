def solution():
    
    price = 30
    uses_per_week = 3
    weeks_used = 2
    total_uses = uses_per_week * weeks_used
    cost_per_use = price / total_uses
    result = cost_per_use
    return result

print(solution())
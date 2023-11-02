def solution():
    
    cost = 30
    uses_per_week = 3
    weeks = 2
    total_uses = uses_per_week * weeks
    cost_per_use = cost / total_uses
    result = cost_per_use
    return result

print(solution())
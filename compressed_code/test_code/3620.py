def solution():
    
    rare_cost = 1
    uncommon_cost = 0.5
    common_cost = 0.25
    rare_cards = 19
    uncommon_cards = 11
    common_cards = 30
    total_cost = (rare_cards * rare_cost) + (uncommon_cards * uncommon_cost) + (common_cards * common_cost)
    result = total_cost
    return result

print(solution())
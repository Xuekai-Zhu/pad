def solution():
    
    rare_cards = 19
    uncommon_cards = 11
    common_cards = 30
    rare_cost = rare_cards * 1
    uncommon_cost = uncommon_cards * 0.5
    common_cost = common_cards * 0.25
    total_cost = rare_cost + uncommon_cost + common_cost
    result = total_cost
    return result

print(solution())
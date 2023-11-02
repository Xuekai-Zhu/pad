def solution():
    
    days_to_save = 22
    savings_per_day = 2
    flower_cost = 4
    total_savings = days_to_save * savings_per_day
    flowers_can_buy = total_savings // flower_cost
    result = flowers_can_buy
    return result

print(solution())
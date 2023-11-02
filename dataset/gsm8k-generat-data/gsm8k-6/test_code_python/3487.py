def solution():
    # Calculate the amount Johnny spends on crab meat in a week
    crab_per_day = 40  # Johnny makes his signature crab dish 40 times a day
    crab_per_week = crab_per_day * 7  # Johnny makes his signature crab dish 7 days a week
    crab_weight_per_week = crab_per_week * 1.5  # Johnny uses 1.5 pounds of crab meat per dish
    crab_cost_per_week = crab_weight_per_week * 8  # Crab meat costs $8 per pound
    days_closed_per_week = 3  # Johnny is closed for 3 days a week
    total_cost_per_week = crab_cost_per_week * (7 - days_closed_per_week)  # Johnny is closed for 3 days a week
    result = total_cost_per_week
    return result

print(solution())
def solution():
    
    muffins_per_dozen = 12
    cost_per_muffin = 0.75
    price_per_muffin = 1.5
    muffins_per_week = muffins_per_dozen * 7
    cost_per_week = muffins_per_week * cost_per_muffin
    revenue_per_week = muffins_per_week * price_per_muffin
    profit_per_week = revenue_per_week - cost_per_week
    result = profit_per_week
    return result

print(solution())
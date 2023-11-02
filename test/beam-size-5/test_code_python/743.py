def solution():
    
    tomatoes_per_day = 500
    cost_per_tomato = 0.5
    new_vendor_price_per_tomato = 0.4
    days_per_week = 7
    total_cost = tomatoes_per_day * cost_per_tomato * days_per_week
    total_new_vendor_cost = tomatoes_per_day * new_vendor_price_per_tomato * days_per_week
    savings = total_cost - total_new_vendor_cost
    result = savings
    return result

print(solution())
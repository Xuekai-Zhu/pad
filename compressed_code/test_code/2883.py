def solution():
    
    initial_cost = 100000
    daily_cost = initial_cost * 0.01
    daily_revenue = 150 * 10
    days_to_break_even = initial_cost / (daily_revenue - daily_cost)
    result = days_to_break_even
    return result

print(solution())
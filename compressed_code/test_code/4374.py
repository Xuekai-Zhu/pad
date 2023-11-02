def solution():
    
    rate = 14
    hours_per_day = 2
    days_per_week = 7
    total_hours = hours_per_day * days_per_week
    total_earnings = rate * total_hours
    shoes_cost = total_earnings / 2
    remaining_money = (total_earnings - shoes_cost) / 2
    result = remaining_money
    return result

print(solution())
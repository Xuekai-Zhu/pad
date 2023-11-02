def solution():
    
    earnings_per_hour = 460 / 23
    total_earnings = earnings_per_hour * (23 + 8)
    total_savings = total_earnings - 340
    remaining_cost = 600 - total_savings
    hours_needed = remaining_cost / earnings_per_hour
    result = hours_needed
    return result

print(solution())
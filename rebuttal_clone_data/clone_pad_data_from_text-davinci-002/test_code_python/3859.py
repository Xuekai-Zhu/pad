def solution():
    days_closed = 3
    daily_revenue = 5000
    days_closed_per_year = days_closed * 6
    total_revenue_lost = daily_revenue * days_closed_per_year
    result = total_revenue_lost
    return result

print(solution())
def solution():
    
    visits_per_month = 30000
    days_per_month = 30
    revenue_per_visit = 0.01
    total_revenue_per_month = visits_per_month * revenue_per_visit
    revenue_per_day = total_revenue_per_month / days_per_month
    result = revenue_per_day
    return result

print(solution())
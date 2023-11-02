def solution():
    visits_per_month = 30000
    revenue_per_visit = 0.01
    days_per_month = 30

    # Calculate the total revenue for the month
    total_revenue = visits_per_month * revenue_per_visit

    # Calculate the revenue per day
    revenue_per_day = total_revenue / days_per_month
    result = revenue_per_day
    return result

print(solution())
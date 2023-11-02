def solution():
    
    weekly_rate = 280
    monthly_rate = 1000
    num_weeks_per_month = 4
    num_months = 3
    total_weekly_cost = weekly_rate * num_weeks_per_month * num_months
    total_monthly_cost = monthly_rate * num_months
    amount_saved = total_weekly_cost - total_monthly_cost
    result = amount_saved
    return result

print(solution())
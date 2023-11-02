def solution():
    weekly_rate = 280
    monthly_rate = 1000
    num_months = 3
    num_weeks_per_month = 4

    # Calculate the total cost of staying for 3 months by paying weekly
    total_weekly_cost = weekly_rate * num_weeks_per_month * num_months

    # Calculate the total cost of staying for 3 months by paying monthly
    total_monthly_cost = monthly_rate * num_months

    # Calculate the amount saved by paying monthly
    amount_saved = total_weekly_cost - total_monthly_cost
    result = amount_saved
    return result

print(solution())
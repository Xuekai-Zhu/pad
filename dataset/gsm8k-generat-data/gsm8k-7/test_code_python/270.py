def solution():
    num_customers_per_week = 50
    num_minutes_per_call = 60
    cost_per_minute = 0.05
    num_weeks_per_month = 4

    # Calculate the total number of minutes Ayla spends on calls in a week
    total_minutes_per_week = num_customers_per_week * num_minutes_per_call

    # Calculate the total cost of calls in a week
    total_cost_per_week = total_minutes_per_week * cost_per_minute

    # Calculate the total cost of calls in a month
    total_cost_per_month = total_cost_per_week * num_weeks_per_month
    result = total_cost_per_month
    return result

print(solution())
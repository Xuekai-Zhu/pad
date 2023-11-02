def solution():
    time_per_call = 60  # Each call lasts for 1 hour, which is 60 minutes
    cost_per_minute = 0.05  # Each minute costs five cents
    customers_per_week = 50
    weeks_per_month = 4

    # Calculate the total cost of all phone calls for the month
    total_time = customers_per_week * time_per_call * weeks_per_month
    total_cost = total_time * cost_per_minute

    result = total_cost
    return result

print(solution())
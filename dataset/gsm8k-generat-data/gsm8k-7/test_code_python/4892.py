def solution():
    trip_cost = 7000
    bills_cost = 3500
    savings_per_month = 500
    num_months = 24

    # Calculate Liam's total savings
    total_savings = savings_per_month * num_months

    # Calculate Liam's remaining savings after paying bills and trip cost
    remaining_savings = total_savings - bills_cost - trip_cost
    result = remaining_savings
    return result

print(solution())
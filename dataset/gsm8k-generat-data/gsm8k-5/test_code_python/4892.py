def solution():
    trip_cost = 7000  # Liam's trip costs $7,000
    bill_cost = 3500  # Liam's bills cost $3,500
    savings_per_month = 500  # Liam saves $500 per month
    months_saved = 24  # Liam has saved for 2 years (24 months)

    # Calculate Liam's total savings
    total_savings = savings_per_month * months_saved

    # Calculate Liam's remaining savings after paying his bills and trip cost
    remaining_savings = total_savings - bill_cost - trip_cost
    result = remaining_savings
    return result

print(solution())
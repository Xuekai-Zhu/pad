def solution():
    monthly_savings = 25
    num_months = 24
    car_repair_cost = 400

    # Calculate the total amount saved over 2 years
    total_saved = monthly_savings * num_months

    # Subtract the cost of the car repair from the total savings
    remaining_balance = total_saved - car_repair_cost
    result = remaining_balance
    return result

print(solution())
def solution():
    current_bill = 50
    increase_percentage = 0.10  # 10% increase
    num_months = 12

    # Calculate the new monthly bill after the increase
    new_monthly_bill = current_bill * (1 + increase_percentage)

    # Calculate the total bill for the entire next year
    total_bill = new_monthly_bill * num_months
    result = total_bill
    return result

print(solution())
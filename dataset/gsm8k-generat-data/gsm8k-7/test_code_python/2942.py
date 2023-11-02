def solution():
    monthly_payment = 150.0
    num_years = 5
    num_months = num_years * 12

    # Calculate the total amount paid for the tractor over the 5 year period
    total_paid = monthly_payment * num_months

    # Calculate the original financing amount
    financing_amount = total_paid
    result = financing_amount
    return result

print(solution())
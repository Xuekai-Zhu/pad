def solution():
    monthly_bill = 50  # Gillian's monthly phone bill is $50
    increase_percentage = 0.1  # Her bill will increase by 10%
    months_in_year = 12  # There are 12 months in a year

    # Calculate the new monthly bill with the increase
    new_monthly_bill = monthly_bill + (monthly_bill * increase_percentage)

    # Calculate the total phone bill for the entire next year
    total_bill = new_monthly_bill * months_in_year
    result = total_bill
    return result

print(solution())
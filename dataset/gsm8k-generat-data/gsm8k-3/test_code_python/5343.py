def solution():
    """Gillian’s phone bill is usually $50 a month. If the monthly bill increases by 10%, what will be her phone bill for the entire next year?"""
    # Define the monthly bill and the percentage increase
    monthly_bill = 50
    percent_increase = 0.1

    # Calculate the new monthly bill including the increase
    new_monthly_bill = monthly_bill * (1 + percent_increase)

    # Calculate the total bill for the next year (12 months)
    total_bill = new_monthly_bill * 12

    # Display the total bill for the next year
    result = total_bill
    return result

print(solution())
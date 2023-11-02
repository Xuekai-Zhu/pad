def solution():
    """Irene earns $500 if she works for 40 hours a week and gets an extra $20 for every hour of overtime. If she worked 50 hours last week, calculate her total income."""
    # Define the regular pay rate and overtime pay rate
    regular_rate = 500 / 40
    overtime_rate = regular_rate + 20

    # Calculate the regular pay and overtime pay
    regular_pay = regular_rate * 40
    overtime_pay = overtime_rate * 10

    # Calculate the total income
    total_income = regular_pay + overtime_pay

    # return the result
    result = total_income
    return result

print(solution())
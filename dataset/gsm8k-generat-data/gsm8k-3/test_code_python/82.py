def solution():
    """Irene earns $500 if she works for 40 hours a week and gets an extra $20 for every hour of overtime. If she worked 50 hours last week, calculate her total income."""
    # Define Irene's regular working hours and pay rate
    regular_hours = 40
    regular_pay = 500

    # Define Irene's overtime pay rate
    overtime_pay = 20

    # Determine the number of overtime hours worked
    overtime_hours = 50 - regular_hours

    # Calculate Irene's total income
    total_income = regular_pay + (overtime_hours * overtime_pay)

    result = total_income
    return result

print(solution())
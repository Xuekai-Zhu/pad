def solution():
    # Calculate Irene's total income for the week
    regular_pay = 500  # Irene earns $500 for working 40 hours a week
    overtime_hours = 50 - 40  # Irene worked 10 hours of overtime
    overtime_pay = overtime_hours * 20  # Irene earns an extra $20 for every hour of overtime worked
    total_income = regular_pay + overtime_pay  # Irene's total income
    result = total_income
    return result

print(solution())
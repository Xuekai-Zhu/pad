def solution():
    base_pay = 500  # Irene earns $500 for working 40 hours in a week
    overtime_pay = 20  # Irene earns an extra $20 per hour for working overtime
    regular_hours = 40  # Irene worked 40 regular hours
    overtime_hours = 10  # Irene worked 10 overtime hours (50 total hours - 40 regular hours)

    # Calculate Irene's total income
    total_income = base_pay + (overtime_hours * overtime_pay)
    result = total_income
    return result

print(solution())
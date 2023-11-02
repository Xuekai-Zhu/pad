def solution():
    # Calculate Mark's new hourly wage after the raise
    new_hourly_wage = 40 * 1.05

    # Calculate Mark's gross weekly income after the raise
    gross_income = new_hourly_wage * 8 * 5

    # Calculate Mark's total expenses per week, including the personal trainer
    total_expenses = 600 + 100

    # Calculate Mark's net income after subtracting his expenses
    net_income = gross_income - total_expenses
    result = net_income
    return result

print(solution())
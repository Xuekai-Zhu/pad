def solution():
    num_employees = 20  # The factory has 20 employees
    shirts_per_employee = 20  # Each employee makes 20 shirts per day
    hours_worked = 8  # The employees work 8-hour shifts
    hourly_wage = 12  # The employees are paid $12 per hour
    payout_per_shirt = 5  # The employees are paid an additional $5 per shirt they make
    price_per_shirt = 35  # The company sells shirts for $35 each
    nonemployee_expenses = 1000  # The company incurs $1000 nonemployee expenses per day

    # Calculate the total number of shirts produced per day
    total_shirts = num_employees * shirts_per_employee

    # Calculate the total amount paid to employees per day
    employee_wages = num_employees * hourly_wage * hours_worked
    employee_payouts = total_shirts * payout_per_shirt
    total_employee_pay = employee_wages + employee_payouts

    # Calculate the total revenue from selling shirts per day
    total_revenue = total_shirts * price_per_shirt

    # Calculate the daily profit
    daily_profit = total_revenue - total_employee_pay - nonemployee_expenses
    result = daily_profit
    return result

print(solution())
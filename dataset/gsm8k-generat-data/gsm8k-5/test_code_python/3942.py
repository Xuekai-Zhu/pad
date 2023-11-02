def solution():
    # Calculate the firefighter's weekly salary
    weekly_salary = 30 * 48

    # Calculate the firefighter's monthly salary
    monthly_salary = weekly_salary * 4

    # Calculate the firefighter's expenses
    rent = monthly_salary / 3
    food = 500
    taxes = 1000
    total_expenses = rent + food + taxes

    # Calculate the firefighter's total savings after paying expenses
    total_savings = monthly_salary - total_expenses
    result = total_savings
    return result

print(solution())
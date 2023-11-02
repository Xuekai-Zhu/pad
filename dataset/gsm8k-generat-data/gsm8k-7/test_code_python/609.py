def solution():
    monthly_contribution = 42
    monthly_salary = 80
    remaining_balance = 18

    # Calculate the total expenses for the household
    total_expenses = monthly_contribution + monthly_salary + remaining_balance

    # Calculate the amount of taxes that Angie paid this month
    taxes_paid = total_expenses - monthly_contribution - monthly_salary
    result = taxes_paid
    return result

print(solution())
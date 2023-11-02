def solution():
    # Define the monthly contribution and salary
    necessities_contribution = 42
    salary = 80

    # Calculate the total income for the month
    total_income = necessities_contribution + salary

    # Calculate the total expenses for the month
    total_expenses = total_income - 18

    # Calculate the amount paid in taxes
    taxes = total_expenses - necessities_contribution - salary

    result = taxes
    return result

print(solution())
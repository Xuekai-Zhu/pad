def solution():
    rent = 600
    food = (3/5) * rent
    mortgage = 3 * food
    savings = 2000
    taxes = (2/5) * savings

    # Calculate total monthly expenses
    expenses = rent + food + mortgage + taxes

    # Calculate gross monthly salary
    gross_salary = expenses + savings
    result = gross_salary
    return result

print(solution())
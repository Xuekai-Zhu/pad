def solution():
    necessities = 42  # Angie contributes $42 a month for necessities
    salary = 80  # Angie has a salary of $80 per month
    remaining = 18  # Angie had $18 left over at the end of the month
    total_expenses = necessities + salary + remaining  # Angie's total expenses for the month

    # Calculate the amount paid in taxes
    taxes = total_expenses - (necessities + salary)
    result = taxes
    return result

print(solution())
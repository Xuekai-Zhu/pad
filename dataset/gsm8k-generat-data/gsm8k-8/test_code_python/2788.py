def solution():
    # Define the variables
    salary = 6000
    rent = 640
    food = 380
    utilities = salary / 4
    insurance = salary / 5

    # Calculate the total expenses
    total_expenses = rent + food + utilities + insurance

    # Calculate the remaining amount
    remaining_amount = salary - total_expenses
    result = remaining_amount
    return result

print(solution())
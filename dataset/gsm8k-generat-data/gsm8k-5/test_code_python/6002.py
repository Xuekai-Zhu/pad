def solution():
    # Calculate Kathryn's monthly expenses on food and travel
    expenses_food_travel = 2 * 1200  # Rent is half of the total expenses

    # Calculate the total expenses in a month
    total_expenses = expenses_food_travel + 1200  # Add rent to the food and travel expenses

    # Calculate the remaining salary after expenses
    remaining_salary = 5000 - total_expenses  # Subtract total expenses from the monthly salary

    result = remaining_salary
    return result

print(solution())
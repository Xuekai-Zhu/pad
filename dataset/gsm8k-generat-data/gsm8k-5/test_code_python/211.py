def solution():
    # Calculate the total expenses from last year
    last_year_expenses = 1000 * 12 + 200 * 12 + 100 * 12

    # Calculate the increased expenses for this year
    rent_increase = 1000 * 0.3
    new_rent = 1000 + rent_increase

    food_increase = 200 * 0.5
    new_food_cost = 200 + food_increase

    insurance_increase = 100 * 3
    new_insurance_cost = 100 + insurance_increase

    new_year_expenses = new_rent * 12 + new_food_cost * 12 + new_insurance_cost * 12

    # Calculate the difference in expenses between the two years
    expenses_difference = new_year_expenses - last_year_expenses
    result = expenses_difference
    return result

print(solution())
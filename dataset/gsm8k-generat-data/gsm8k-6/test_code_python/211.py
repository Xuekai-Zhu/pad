def solution():
    # Calculate last year's total expenses
    last_year_expenses = (1000+200+100)*12

    # Calculate this year's total expenses
    rent_increase = 0.3 * 1000
    new_rent = 1000 + rent_increase
    food_increase = 0.5 * 200
    new_food_cost = 200 + food_increase
    new_insurance_cost = 3 * 100
    this_year_expenses = (new_rent + new_food_cost + new_insurance_cost) * 12

    # Calculate the difference between this year's and last year's expenses
    expenses_difference = this_year_expenses - last_year_expenses
    result = expenses_difference
    return result

print(solution())
def solution():
    # Calculate last year's total expenses
    last_year_total_expenses = 12*(1000+200+100)

    # Calculate this year's expenses after increases
    rent_increase = 0.3*1000
    new_rent_cost = 1000+rent_increase

    food_increase = 0.5*200
    new_food_cost = 200+food_increase

    insurance_increase = 3*100
    new_insurance_cost = 100+insurance_increase

    this_year_total_expenses = 12*(new_rent_cost+new_food_cost+new_insurance_cost)

    # Calculate the difference between this year's and last year's expenses
    difference = this_year_total_expenses - last_year_total_expenses

    result = difference
    return result

print(solution())
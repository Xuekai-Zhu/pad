def solution():
    weekly_allowance = 30  # Annabelle receives a weekly allowance of $30
    junk_food_cost = weekly_allowance / 3  # Annabelle spent a third of her allowance on junk food
    sweets_cost = 8  # Annabelle spent $8 on sweets
    total_expenses = junk_food_cost + sweets_cost  # Annabelle's total expenses
    amount_saved = weekly_allowance - total_expenses  # Annabelle's savings after expenses
    result = amount_saved
    return result

print(solution())
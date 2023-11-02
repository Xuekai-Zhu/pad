def solution():
    """Annabelle collected a weekly allowance of $30. She spent a third of it buying junk food, then spent another $8 on sweets. Out of guilt she decides to save the rest. How much did she save?"""
    weekly_allowance = 30
    junk_food_spending = weekly_allowance / 3
    sweets_spending = 8
    total_spending = junk_food_spending + sweets_spending
    amount_saved = weekly_allowance - total_spending
    result = amount_saved
    return result

print(solution())
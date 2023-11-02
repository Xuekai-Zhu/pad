def solution():
    """Annabelle collected a weekly allowance of $30. She spent a third of it buying junk food, then spent another $8 on sweets. Out of guilt she decides to save the rest. How much did she save?"""
    allowance = 30
    spent_on_junk_food = allowance / 3
    spent_on_sweets = 8
    saved_amount = allowance - spent_on_junk_food - spent_on_sweets
    result = saved_amount
    return result

print(solution())
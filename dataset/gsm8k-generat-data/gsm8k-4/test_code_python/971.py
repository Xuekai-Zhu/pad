def solution():
    """Annabelle collected a weekly allowance of $30. She spent a third of it buying junk food, then spent another $8 on sweets. Out of guilt she decides to save the rest. How much did she save?"""
    # Define the weekly allowance
    weekly_allowance = 30

    # Calculate the amount spent on junk food
    junk_food_spending = weekly_allowance / 3

    # Calculate the total amount spent, including junk food and sweets
    total_spending = junk_food_spending + 8

    # Calculate the amount saved
    saved_amount = weekly_allowance - total_spending

    # return the result
    result = saved_amount
    return result

print(solution())
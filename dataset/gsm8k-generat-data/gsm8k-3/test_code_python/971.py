def solution():
    """Annabelle collected a weekly allowance of $30. She spent a third of it buying junk food, then spent another $8 on sweets. Out of guilt she decides to save the rest. How much did she save?"""
    # Define the amount of Annabelle's weekly allowance
    weekly_allowance = 30

    # Calculate the amount Annabelle spent on junk food
    junk_food_cost = weekly_allowance / 3

    # Calculate the total amount Annabelle spent
    total_spent = junk_food_cost + 8

    # Calculate the amount Annabelle saved
    saved_amount = weekly_allowance - total_spent

    # Display the amount Annabelle saved
    result = saved_amount
    return result

print(solution())
def solution():
    """Tom receives a $12 allowance per month. In the first week, he spends a third of it; in the second week, he spends a quarter of what he has left. How much money does he have left to finish the month?"""
    # Define the initial allowance and the amount spent in the first week
    initial_allowance = 12
    first_week_spending = initial_allowance / 3

    # Calculate the amount left after the first week
    amount_left = initial_allowance - first_week_spending

    # Calculate the amount spent in the second week
    second_week_spending = amount_left / 4

    # Calculate the amount left after the second week
    amount_left -= second_week_spending

    # Return the amount left at the end of the month
    result = round(amount_left, 2)
    return result

print(solution())
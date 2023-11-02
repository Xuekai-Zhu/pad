def solution():
    """Rachel earned $200 babysitting. She spent 1/4 of the money on lunch. She spent 1/2 of the money on a DVD. How much did Rachel have left?"""
    # Define the amount of money Rachel earned
    money_earned = 200

    # Calculate the amount of money spent on lunch
    lunch_spending = money_earned / 4

    # Calculate the amount of money spent on a DVD
    dvd_spending = money_earned / 2

    # Calculate the amount of money Rachel has left
    money_left = money_earned - lunch_spending - dvd_spending

    result = money_left
    return result

print(solution())
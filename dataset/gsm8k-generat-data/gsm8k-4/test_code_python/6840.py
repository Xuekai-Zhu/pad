def solution():
    """Bob started out the week with $80. On Monday alone, he spent half the money. On Tuesday, he spent one-fifth of the amount left from Monday. On Wednesday, he spent 3/8ths of the amount left from Tuesday. How much does he have left now?"""
    # Define Bob's initial amount of money
    initial_money = 80

    # Calculate the money spent on Monday
    monday_spending = initial_money / 2

    # Calculate the amount left after Monday
    left_after_monday = initial_money - monday_spending

    # Calculate the money spent on Tuesday
    tuesday_spending = left_after_monday / 5

    # Calculate the amount left after Tuesday
    left_after_tuesday = left_after_monday - tuesday_spending

    # Calculate the money spent on Wednesday
    wednesday_spending = left_after_tuesday * (3/8)

    # Calculate the amount left after Wednesday
    left_after_wednesday = left_after_tuesday - wednesday_spending

    result = left_after_wednesday
    return result

print(solution())
def solution():
    """Reese had a sum of money in her savings account. The company she used to work with was not doing well which is why she lost her job. So she spent 20% of her savings for her expenses in February, 40% of it in March, and $1500 in April. How much did she have in her savings account if she still has $2900 after spending those amounts?"""
    # Define the final amount in Reese's savings account
    final_amount = 2900

    # Calculate the amount she spent in April
    april_expense = 1500

    # Calculate the percentage of her savings she had left after April
    left_after_april = (final_amount + april_expense) / 0.6

    # Calculate the total amount she had in her savings account initially
    initial_amount = left_after_april / 0.8

    result = initial_amount
    return result

print(solution())
def solution():
    """Joanna has $8. Compared to her money, her brother has thrice as much while her sister has only half as much. How much money do the three of them have altogether?"""
    # Define Joanna's money
    joanna_money = 8

    # Calculate the amount of money Joanna's brother has
    brother_money = 3 * joanna_money

    # Calculate the amount of money Joanna's sister has
    sister_money = joanna_money / 2

    # Calculate the total amount of money the three of them have together
    total_money = joanna_money + brother_money + sister_money

    # return the result
    result = total_money
    return result

print(solution())
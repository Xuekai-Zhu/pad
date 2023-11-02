def solution():
    """Joanna has $8. Compared to her money, her brother has thrice as much while her sister has only half as much. How much money do the three of them have altogether?"""
    # Define the amount of money Joanna has
    joanna_money = 8

    # Calculate the amount of money her brother has
    brother_money = 3 * joanna_money

    # Calculate the amount of money her sister has
    sister_money = joanna_money / 2

    # Calculate the total amount of money the three of them have
    total_money = joanna_money + brother_money + sister_money

    # Display the total amount of money
    result = total_money
    return result

print(solution())
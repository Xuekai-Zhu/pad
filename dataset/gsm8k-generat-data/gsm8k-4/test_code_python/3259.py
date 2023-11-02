def solution():
    """Michael has $42. Michael gives away half the money to his brother. His brother then buys 3 dollars worth of candy. If his brother has $35 left, how much money, in dollars, did his brother have at first?"""
    # Define the initial amount of money Michael has
    michael_money = 42

    # Calculate the amount of money Michael gives to his brother
    brother_money = michael_money / 2

    # Calculate the amount of money Brother has left after buying candy
    brother_left = 35
    brother_spent = 3
    brother_before_spent = brother_left + brother_spent

    # Calculate the initial amount of money Brother had
    brother_initial = brother_before_spent + brother_money

    # Return the result
    result = brother_initial
    return result

print(solution())
def solution():
    """Michael has $42. His brother has $17. Michael gives away half the money to his brother. His brother then buys 3 dollars worth of candy. How much money, in dollars, did his brother have in the end?"""
    # Define the initial amounts of money
    michael_money = 42
    brother_money = 17

    # Calculate the amount of money Michael gives to his brother
    michael_to_brother = michael_money / 2

    # Add the money from Michael to his brother's total
    brother_money += michael_to_brother

    # Subtract the cost of candy from his brother's total
    brother_money -= 3

    # Return the final amount of money his brother has
    result = brother_money
    return result

print(solution())
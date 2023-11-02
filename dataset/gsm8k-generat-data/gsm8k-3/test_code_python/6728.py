def solution():
    """Michael has $42. His brother has $17. Michael gives away half the money to his brother. His brother then buys 3 dollars worth of candy. How much money, in dollars, did his brother have in the end?"""
    # Define Michael's initial amount and his brother's initial amount
    michael_money = 42
    brother_money = 17

    # Calculate the amount of money Michael gave to his brother
    michael_half_money = michael_money / 2

    # Add the half of Michael's money to his brother's initial amount
    brother_money += michael_half_money

    # Subtract the amount his brother spent on candy
    brother_money -= 3

    # Display the final amount of money his brother had
    result = brother_money
    return result

print(solution())
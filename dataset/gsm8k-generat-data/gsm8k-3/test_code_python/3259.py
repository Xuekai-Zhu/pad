def solution():
    """Michael has $42. Michael gives away half the money to his brother. His brother then buys 3 dollars worth of candy. If his brother has $35 left, how much money, in dollars, did his brother have at first?"""
    # Michael gives away half his money, so his brother receives 42 / 2 = 21 dollars
    brother_money = 21

    # Brother spends 3 dollars on candy, so he has 35 + 3 = 38 dollars left
    brother_money_left = 38

    # Brother's original money can be calculated by adding the money he has now to the money spent on candy and doubling the result
    brother_money_original = (brother_money_left + 3) * 2

    # Display the original amount of money the brother had
    result = brother_money_original
    return result

print(solution())
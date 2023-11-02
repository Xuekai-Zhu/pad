def solution():
    """Tony puts $1,000 in a savings account for 1 year. It earns 20% interest. He then takes out half the money to buy a new TV. The next year, the remaining money earns 15% interest. How much is now in the account?"""
    # Calculate the amount of money after one year with 20% interest
    money_after_first_year = 1000 * 1.2

    # Take out half the money for a new TV
    remaining_money = money_after_first_year / 2

    # Calculate the amount of money after the second year with 15% interest
    money_after_second_year = remaining_money * 1.15

    result = money_after_second_year
    return result

print(solution())
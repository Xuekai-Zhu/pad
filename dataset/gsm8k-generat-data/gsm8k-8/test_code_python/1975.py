def solution():
    # Calculate the amount of money in the account after one year with 20% interest
    money_after_1_year = 1000 * 1.2

    # Take out half the money for a new TV
    money_after_TV_purchase = money_after_1_year / 2

    # Calculate the remaining money after the TV purchase
    remaining_money = money_after_1_year - money_after_TV_purchase

    # Calculate the amount of money in the account after two years with 15% interest
    money_after_2_years = remaining_money * 1.15

    result = money_after_2_years
    return result

print(solution())
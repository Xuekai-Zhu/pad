def solution():
    starting_money = 25

    # Subtract the amount given to mom
    left_after_mom = starting_money - 8

    # Calculate the amount invested in the money market
    money_market = left_after_mom / 2

    # Calculate the amount spent on the 5 items at 50 cents each
    amount_spent = 5 * 0.5

    # Calculate the final amount of money Tabitha has left
    final_money = left_after_mom - money_market - amount_spent
    result = final_money
    return result

print(solution())
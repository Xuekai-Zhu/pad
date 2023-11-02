def solution():
    initial_balance = 55

    # Calculate the remaining balance after buying a shirt
    balance_after_shirt = initial_balance - 7

    # Calculate the amount spent on the second shop
    second_shop_spending = 3 * 7

    # Calculate the remaining balance after spending at the second shop
    remaining_balance = balance_after_shirt - second_shop_spending

    result = remaining_balance
    return result

print(solution())
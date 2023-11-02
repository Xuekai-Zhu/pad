def solution():
    # Calculate how many postcards Bernie sold
    sold_postcards = 18 / 2

    # Calculate the amount of money Bernie earned
    money_earned = sold_postcards * 15

    # Calculate how many new postcards Bernie can buy
    new_postcards = money_earned / 5

    # Calculate how many postcards Bernie has after all transactions
    total_postcards = 18 - sold_postcards + new_postcards

    result = total_postcards
    return result

print(solution())
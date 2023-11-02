def solution():
    # Calculate the number of postcards sold by Bernie
    sold_postcards = 18 / 2

    # Calculate the amount of money earned from selling postcards
    money_earned = sold_postcards * 15

    # Calculate the number of postcards Bernie can buy with the earned money
    new_postcards = money_earned / 5

    # Calculate the total number of postcards Bernie has after all transactions
    total_postcards = sold_postcards + new_postcards
    result = total_postcards
    return result

print(solution())
def solution():
    num_postcards = 18
    sell_price = 15
    buy_price = 5
    num_to_sell = num_postcards / 2

    # Calculate the total amount Bernie earns from selling half his collection
    total_earnings = num_to_sell * sell_price

    # Calculate the number of postcards Bernie can buy with his earnings
    num_to_buy = total_earnings / buy_price

    # Calculate the total number of postcards Bernie has after all transactions
    total_postcards = num_postcards - num_to_sell + num_to_buy
    result = total_postcards
    return result

print(solution())
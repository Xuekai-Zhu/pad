def solution():
    # Price of the first bear
    bear_price = 4.00

    # Price of the remaining 100 bears with a discount of 50 cents
    remaining_bears_price = (100 * 0.50)

    # Total price Wally pays for 101 bears
    total_price = bear_price + remaining_bears_price

    result = total_price
    return result

print(solution())
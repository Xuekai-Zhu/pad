def solution():
    # Calculate the price of the frame Yvette initially wanted to buy
    initial_price = 60 / 1.2

    # Calculate the price of the smaller frame Yvette bought
    smaller_price = 0.75 * initial_price

    # Calculate how much money Yvette has remaining
    remaining_money = 60 - smaller_price
    result = remaining_money
    return result

print(solution())
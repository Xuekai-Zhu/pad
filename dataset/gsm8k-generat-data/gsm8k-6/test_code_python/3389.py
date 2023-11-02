def solution():
    # Calculate the current price of RAM
    initial_price = 50
    increased_price = initial_price * 1.3  # the price increased by 30%
    final_price = increased_price * 0.8  # the price fell by 20% from what it has risen after 2 years
    result = final_price
    return result

print(solution())
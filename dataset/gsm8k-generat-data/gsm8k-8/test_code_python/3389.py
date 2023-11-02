def solution():
    # Set the initial price of RAM
    price = 50

    # Increase the price by 30%
    price *= 1.3

    # Wait two years
    # The price is the same now as it was after the fire, so nothing happens here

    # Decrease the price by 20%
    price *= 0.8

    result = price
    return result

print(solution())
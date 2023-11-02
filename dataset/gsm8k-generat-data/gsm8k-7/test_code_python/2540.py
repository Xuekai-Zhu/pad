def solution():
    original_price = 4000
    future_multiplier = 3

    # Calculate the future price of the art piece
    future_price = original_price * future_multiplier

    # Calculate the increase in price
    increase = future_price - original_price
    result = increase
    return result

print(solution())
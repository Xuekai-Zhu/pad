def solution():
    # Define the initial price of the iPhone
    initial_price = 1000

    # Calculate the price after the first 10% discount
    price_after_first_discount = initial_price - 0.1 * initial_price

    # Calculate the price after the second 20% discount
    price_after_second_discount = price_after_first_discount - 0.2 * price_after_first_discount

    result = price_after_second_discount
    return result

print(solution())
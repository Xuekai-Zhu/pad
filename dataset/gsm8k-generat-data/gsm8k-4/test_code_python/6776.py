def solution():
    """Liz sold her car at 80% of what she originally paid. She uses the proceeds of that sale and needs only $4,000 to buy herself a new $30,000 car. How much cheaper is her new car versus what she originally paid for her old one?"""
    # Calculate the amount Liz received from selling her old car
    selling_price = original_price * 0.8

    # Calculate the total amount Liz has available to buy a new car
    total_amount = selling_price + 4000

    # Calculate the difference in price between Liz's old car and her new one
    price_difference = original_price - 30000

    # Convert the price difference to a positive value
    if price_difference < 0:
        price_difference = -price_difference

    # return the result
    result = price_difference
    return result

print(solution())
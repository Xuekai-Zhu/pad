def solution():
    # Define the given values
    units = 18
    paid_price = 500
    discount_percentage = 20

    # Calculate the price of one unit after the discount
    discounted_price = (100 - discount_percentage) / 100 * original_price

    # Calculate the total price before the discount
    original_total_price = units * discounted_price

    # Calculate the original price per unit
    original_price = original_total_price / units

    result = original_price
    return result

print(solution())
def solution():
    pins_to_buy = 10  # John wants to buy 10 pins
    original_price = 20  # The original price per pin is $20
    discount = 0.15  # The pins are on sale for 15% off

    # Calculate the discounted price per pin
    discounted_price = original_price - (original_price * discount)

    # Calculate the total cost of the pins John is buying
    total_cost = pins_to_buy * discounted_price
    result = total_cost
    return result

print(solution())
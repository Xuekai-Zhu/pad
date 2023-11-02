def solution():
    """John decided to buy 10 pins for himself.  They are normally $20 each but they were on sale for 15% off.  How much did he spend on pins?"""
    # Define the regular price and discount
    REGULAR_PRICE = 20
    DISCOUNT = 0.15

    # Calculate the sale price per pin
    sale_price = REGULAR_PRICE - (REGULAR_PRICE * DISCOUNT)

    # Calculate the total cost of the pins
    total_cost = sale_price * 10

    # Display the total cost
    result = total_cost
    return result

print(solution())
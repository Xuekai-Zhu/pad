def solution():
    """John decided to buy 10 pins for himself. They are normally $20 each but they were on sale for 15% off. How much did he spend on pins?"""
    # Define the original price of each pin and the discount percentage
    ORIGINAL_PRICE = 20
    DISCOUNT_PERCENTAGE = 0.15

    # Calculate the discount amount
    discount_amount = ORIGINAL_PRICE * DISCOUNT_PERCENTAGE

    # Calculate the sale price of each pin
    sale_price = ORIGINAL_PRICE - discount_amount

    # Calculate the total cost of the 10 pins
    total_cost = sale_price * 10

    # return the result
    result = total_cost
    return result

print(solution())
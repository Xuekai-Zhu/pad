def solution():
    # Define the sale price and discount percentage
    sale_price = 450
    discount_percentage = 0.1

    # Calculate the original price using the formula:
    # sale price = original price - (discount percentage * original price)
    original_price = sale_price / (1 - discount_percentage)

    result = original_price
    return result

print(solution())
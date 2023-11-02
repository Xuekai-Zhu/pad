def solution():
    # Calculate the sale price of the vase
    original_price = 200
    sale_price = original_price - (0.25 * original_price)

    # Calculate the total price with the sales tax
    total_price = sale_price + (0.1 * sale_price)
    result = total_price
    return result

print(solution())
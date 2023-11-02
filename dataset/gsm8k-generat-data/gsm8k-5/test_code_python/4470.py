def solution():
    original_price = 1200  # The original price of the cabinet is $1200
    discount_rate = 0.15  # Tim gets a 15% discount
    discount_amount = original_price * discount_rate  # Calculate the discount amount
    sale_price = original_price - discount_amount  # Calculate the sale price after the discount

    result = sale_price
    return result

print(solution())
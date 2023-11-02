def solution():
    original_price = 80  # The original price of the shirt is $80
    discount = 0.15  # The special discount is 15%
    discount_amount = original_price * discount  # Calculate the discount amount
    sale_price = original_price - discount_amount  # Calculate the sale price after the discount
    result = sale_price
    return result

print(solution())
def solution():
    original_price = 100  # Last week the price of a movie ticket was $100
    discount_percentage = 20  # The price is down by 20%
    discount_amount = original_price * (discount_percentage / 100)  # Calculate the discount amount
    new_price = original_price - discount_amount  # Calculate the new price after discount
    result = new_price
    return result

print(solution())
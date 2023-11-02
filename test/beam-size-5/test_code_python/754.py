def solution():
    original_price = 140  # The bag is marked $140
    discount_percentage = 5  # The bag has a 5% discount
    discount_amount = original_price * (discount_percentage / 100)  # Calculate the discount amount
    discounted_price = original_price - discount_amount  # Calculate the discounted price
    result = discounted_price
    return result

print(solution())
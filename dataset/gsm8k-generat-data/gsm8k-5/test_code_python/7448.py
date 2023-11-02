def solution():
    original_price = 120  # The original price of the bedside lamp is $120
    discount_percentage = 20  # The department store is offering a 20% discount on all fixtures
    discount_amount = original_price * (discount_percentage / 100)  # Calculate the discount amount
    discounted_price = original_price - discount_amount  # Calculate the discounted price
    result = discounted_price
    return result

print(solution())
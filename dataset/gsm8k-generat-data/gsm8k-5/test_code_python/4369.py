def solution():
    original_price = 10  # The original price of the plant is $10
    discount_percentage = 10  # Rose gets a 10% discount
    discount_amount = original_price * (discount_percentage / 100)  # Calculate the discount amount
    discounted_price = original_price - discount_amount  # Calculate the discounted price after the discount

    result = discounted_price
    return result

print(solution())
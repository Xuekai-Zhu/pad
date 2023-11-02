def solution():
    original_price = 20  # The original price of the t-shirt is $20
    discount_percentage = 50  # All items are 50% off
    discount = original_price * (discount_percentage / 100)  # Calculate the discount
    discounted_price = original_price - discount  # Calculate the discounted price
    total_spent = discounted_price * 4  # Each friend buys one t-shirt, so they spend a total of 4 t-shirts x discounted price
    result = total_spent
    return result

print(solution())
def solution():
    original_price = 60  # James paid $60 for 3 shirts
    num_shirts = 3  # James bought 3 shirts
    discount_percentage = 40  # There is a 40% discount on the shirts

    # Calculate the discounted price for the 3 shirts
    discounted_price = original_price * (1 - (discount_percentage / 100))
    price_per_shirt = discounted_price / num_shirts
    result = price_per_shirt
    return result

print(solution())
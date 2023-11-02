def solution():
    original_price = 7.50  # Carla's order costs $7.50
    coupon = 2.50  # Carla has a coupon for $2.50
    price_after_coupon = original_price - coupon  # Calculate the price after applying the coupon
    senior_discount = 0.20  # Carla gets a 20% discount for being a senior citizen
    price_after_discount = price_after_coupon * (1 - senior_discount)  # Calculate the price after applying the senior citizen discount
    result = price_after_discount
    return result

print(solution())
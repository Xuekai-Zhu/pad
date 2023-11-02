def solution():
    """Hannah is buying some apples for $5 per kilogram. If she would get a 40% discount on each kilogram of apples, how much would she pay for 10 kilograms of them?"""
    apple_price_per_kg = 5
    discount = 0.4
    discounted_price_per_kg = apple_price_per_kg - (apple_price_per_kg * discount)
    total_price = discounted_price_per_kg * 10
    result = total_price
    return result

print(solution())
def solution():
    """Hannah is buying some apples for $5 per kilogram. If she would get a 40% discount on each kilogram of apples, how much would she pay for 10 kilograms of them?"""
    price_per_kilogram = 5
    discount_percent = 40
    discounted_price = price_per_kilogram * (100 - discount_percent) / 100
    total_price = discounted_price * 10
    result = total_price
    return result

print(solution())
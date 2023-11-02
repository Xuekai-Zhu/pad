def solution():
    """Sansa is a famous artist, she can draw a portrait and sell it according to its size. She sells an 8-inch portrait for $5, and a 16-inch portrait for twice the price of the 8-inch portrait. If she sells three 8-inch portraits and five 16-inch portraits per day, how many does she earns every 3 days?"""
    price_8_inch = 5
    price_16_inch = 2 * price_8_inch
    sold_8_inch = 3
    sold_16_inch = 5
    total_earnings_per_day = (price_8_inch * sold_8_inch) + (price_16_inch * sold_16_inch)
    total_earnings_per_3_days = total_earnings_per_day * 3
    result = total_earnings_per_3_days
    return result

print(solution())
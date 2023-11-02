def solution():
    """Sansa is a famous artist, she can draw a portrait and sell it according to its size. She sells an 8-inch portrait for $5, and a 16-inch portrait for twice the price of the 8-inch portrait. If she sells three 8-inch portraits and five 16-inch portraits per day, how many does she earns every 3 days?"""
    price_8_inch = 5
    price_16_inch = price_8_inch * 2
    num_8_inch_per_day = 3
    num_16_inch_per_day = 5
    earnings_per_day = (num_8_inch_per_day * price_8_inch) + (num_16_inch_per_day * price_16_inch)
    earnings_per_3_days = earnings_per_day * 3
    result = earnings_per_3_days
    return result

print(solution())
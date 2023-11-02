def solution():
    
    price_8_inch = 5
    price_16_inch = price_8_inch * 2
    num_8_inch_per_day = 3
    num_16_inch_per_day = 5
    earnings_per_day = (num_8_inch_per_day * price_8_inch) + (num_16_inch_per_day * price_16_inch)
    earnings_per_3_days = earnings_per_day * 3
    result = earnings_per_3_days
    return result

print(solution())
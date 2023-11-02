def solution():
    
    price_8_inch = 5
    price_16_inch = 2 * price_8_inch
    sold_8_inch = 3
    sold_16_inch = 5
    total_earnings_per_day = (price_8_inch * sold_8_inch) + (price_16_inch * sold_16_inch)
    total_earnings_per_3_days = total_earnings_per_day * 3
    result = total_earnings_per_3_days
    return result

print(solution())
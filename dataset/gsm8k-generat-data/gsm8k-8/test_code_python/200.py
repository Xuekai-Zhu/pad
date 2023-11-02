def solution():
    # Define the prices of the portraits
    price_8_inch = 5
    price_16_inch = 2 * price_8_inch

    # Define the number of portraits sold per day
    num_8_inch_per_day = 3
    num_16_inch_per_day = 5

    # Calculate the earnings per day
    earnings_per_day = (num_8_inch_per_day * price_8_inch) + (num_16_inch_per_day * price_16_inch)

    # Calculate the earnings per 3 days
    earnings_per_3_days = earnings_per_day * 3

    result = earnings_per_3_days
    return result

print(solution())
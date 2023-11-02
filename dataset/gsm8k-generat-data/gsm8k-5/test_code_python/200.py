def solution():
    # Calculate the price of a 16-inch portrait
    price_16_inches = 2 * 5  # Twice the price of an 8-inch portrait

    # Calculate the daily earnings from selling 3 8-inch portraits and 5 16-inch portraits
    earnings_daily = (3 * 5) + (5 * price_16_inches)

    # Calculate the total earnings over 3 days
    earnings_3_days = earnings_daily * 3
    result = earnings_3_days
    return result

print(solution())
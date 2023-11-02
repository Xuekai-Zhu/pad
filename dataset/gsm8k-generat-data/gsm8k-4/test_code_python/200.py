def solution():
    """Sansa is a famous artist, she can draw a portrait and sell it according to its size. She sells an 8-inch portrait for $5, and a 16-inch portrait for twice the price of the 8-inch portrait. If she sells three 8-inch portraits and five 16-inch portraits per day, how many does she earns every 3 days?"""
    # Define the prices of the portraits
    small_portrait_price = 5
    large_portrait_price = 2 * small_portrait_price

    # Calculate the daily earnings from selling small portraits
    small_portrait_earnings = 3 * small_portrait_price

    # Calculate the daily earnings from selling large portraits
    large_portrait_earnings = 5 * large_portrait_price

    # Calculate the total earnings per day
    total_earnings = small_portrait_earnings + large_portrait_earnings

    # Calculate the total earnings per 3 days
    total_earnings_3_days = total_earnings * 3

    # return the result
    result = total_earnings_3_days
    return result

print(solution())
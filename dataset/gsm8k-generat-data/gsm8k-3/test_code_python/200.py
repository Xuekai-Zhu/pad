def solution():
    """Sansa is a famous artist, she can draw a portrait and sell it according to its size. She sells an 8-inch portrait for $5, and a 16-inch portrait for twice the price of the 8-inch portrait. If she sells three 8-inch portraits and five 16-inch portraits per day, how much does she earn every 3 days?"""
    # Define the price of an 8-inch portrait
    small_price = 5

    # Define the price of a 16-inch portrait
    large_price = 2 * small_price

    # Calculate the earnings from selling 8-inch portraits each day
    small_earnings_per_day = small_price * 3

    # Calculate the earnings from selling 16-inch portraits each day
    large_earnings_per_day = large_price * 5

    # Calculate the total earnings over 3 days
    total_earnings = (small_earnings_per_day + large_earnings_per_day) * 3

    # return the result
    result = total_earnings
    return result

print(solution())
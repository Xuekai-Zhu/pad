def solution():
    """Keaton has a farm of oranges and apples. He can harvest his oranges every 2 months and can sell the harvest for $50. He can harvest his apples every 3 months and can sell this harvest for $30. How much money can Keaton earn every year?"""
    # Define the selling price and harvest intervals for oranges and apples
    ORANGE_PRICE = 50
    ORANGE_INTERVAL = 2
    APPLE_PRICE = 30
    APPLE_INTERVAL = 3

    # Calculate the number of harvests per year for oranges and apples
    orange_harvests_per_year = 12 // ORANGE_INTERVAL
    apple_harvests_per_year = 12 // APPLE_INTERVAL

    # Calculate the total earnings from oranges and apples
    orange_earnings = ORANGE_PRICE * orange_harvests_per_year
    apple_earnings = APPLE_PRICE * apple_harvests_per_year

    # Calculate the total earnings for the year
    total_earnings = orange_earnings + apple_earnings

    result = total_earnings
    return result

print(solution())
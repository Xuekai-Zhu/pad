def solution():
    """Keaton has a farm of oranges and apples. He can harvest his oranges every 2 months and can sell the harvest for $50.  He can harvest his apples every 3 months and can sell this harvest for $30. How much money can Keaton earn every year?"""
    # Define the price for each type of harvest
    ORANGE_PRICE = 50
    APPLE_PRICE = 30

    # Calculate the number of harvests per year
    oranges_per_year = 12 // 2  # 12 months in a year, harvest every 2 months
    apples_per_year = 12 // 3  # 12 months in a year, harvest every 3 months

    # Calculate the total earnings per year
    total_earnings = oranges_per_year * ORANGE_PRICE + apples_per_year * APPLE_PRICE

    # Display the total earnings
    result = total_earnings
    return result

print(solution())
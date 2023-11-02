def solution():
    """Laran has started a poster business. She is selling 5 posters per day at school. Two posters per day are her large posters that sell for $10. The large posters cost her $5 to make. The remaining posters are small posters that sell for $6. They cost $3 to produce. How much profit, in dollars, does Laran make per 5-day school week?"""
    # Define the number of days in the school week and the number of posters sold each day
    DAYS_IN_WEEK = 5
    POSTERS_PER_DAY = 5
    
    # Define the prices and costs of the posters
    LARGE_POSTER_PRICE = 10
    LARGE_POSTER_COST = 5
    SMALL_POSTER_PRICE = 6
    SMALL_POSTER_COST = 3
    
    # Calculate the profit from selling large posters
    large_poster_profit = (LARGE_POSTER_PRICE - LARGE_POSTER_COST) * 2
    
    # Calculate the profit from selling small posters
    small_poster_profit = (SMALL_POSTER_PRICE - SMALL_POSTER_COST) * (POSTERS_PER_DAY - 2)
    
    # Calculate the total profit for each day
    daily_profit = large_poster_profit + small_poster_profit
    
    # Calculate the total profit for the school week
    weekly_profit = daily_profit * DAYS_IN_WEEK
    
    result = weekly_profit
    return result

print(solution())
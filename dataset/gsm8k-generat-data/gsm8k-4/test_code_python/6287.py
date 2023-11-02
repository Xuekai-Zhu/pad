def solution():
    """John can produce 1000 tires a day. It cost $250 to produce each tire. He manages to sell them for 1.5 times as much. He could sell 1200 tires a day if his factory was able to produce more. How much money does he lose out a week by not being able to produce all the tires?"""
    # Define the daily production and cost per tire
    DAILY_PRODUCTION = 1000
    COST_PER_TIRE = 250

    # Calculate the selling price per tire
    SELLING_PRICE = 1.5 * COST_PER_TIRE

    # Calculate the daily profit
    daily_profit = (SELLING_PRICE - COST_PER_TIRE) * DAILY_PRODUCTION

    # Calculate the profit lost due to not being able to produce more tires
    lost_profit = (1200 - DAILY_PRODUCTION) * daily_profit

    # Calculate the weekly lost profit
    weekly_lost_profit = lost_profit * 7

    result = weekly_lost_profit
    return result

print(solution())
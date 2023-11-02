def solution():
    """John can produce 1000 tires a day.  It cost $250 to produce each tire.  He manages to sell them for 1.5 times as much.  He could sell 1200 tires a day if his factory was able to produce more.  How much money does he lose out a week by not being able to produce all the tires?"""
    # Define the number of tires John can produce and sell per day
    PRODUCTION_CAPACITY = 1000
    SELLING_CAPACITY = 1200

    # Define the cost of producing one tire and the selling price of one tire
    COST_PER_TIRE = 250
    SELLING_PRICE_PER_TIRE = 1.5 * COST_PER_TIRE

    # Calculate the profit per tire
    PROFIT_PER_TIRE = SELLING_PRICE_PER_TIRE - COST_PER_TIRE

    # Calculate the total profit John could make per day if he could produce and sell all the tires
    MAX_PROFIT_PER_DAY = SELLING_CAPACITY * PROFIT_PER_TIRE

    # Calculate the profit John is losing out on per day by not being able to produce and sell all the tires
    LOST_PROFIT_PER_DAY = (SELLING_CAPACITY - PRODUCTION_CAPACITY) * PROFIT_PER_TIRE

    # Calculate the total profit John is losing out on per week
    LOST_PROFIT_PER_WEEK = LOST_PROFIT_PER_DAY * 7

    # Display the total profit John is losing out on per week
    result = LOST_PROFIT_PER_WEEK
    return result

print(solution())
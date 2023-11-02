def solution():
    """John is a door-to-door salesman.  He visits 50 houses a day.  20% of them buy something from them.  Of those that buy something half buy a $50 set of knives and the other half buy a $150 set of knives.  How much does he sell a week when he works 5 days a week?"""
    # Define the number of houses John visits in a day
    HOUSES_PER_DAY = 50

    # Define the percent of houses that buy something from John
    BUY_PERCENT = 0.2

    # Define the cost of each set of knives
    SMALL_SET_COST = 50
    LARGE_SET_COST = 150

    # Calculate the number of houses that buy something from John in a day
    houses_buying = int(HOUSES_PER_DAY * BUY_PERCENT)

    # Calculate the number of houses that buy the small set of knives in a day
    small_set_buyers = int(houses_buying / 2)

    # Calculate the number of houses that buy the large set of knives in a day
    large_set_buyers = int(houses_buying / 2)

    # Calculate the total sales in a day
    daily_sales = (small_set_buyers * SMALL_SET_COST) + (large_set_buyers * LARGE_SET_COST)

    # Calculate the weekly sales
    weekly_sales = daily_sales * 5

    # Display the weekly sales
    result = weekly_sales
    return result

print(solution())
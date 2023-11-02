def solution():
    """William's class set a goal each week of the number of cans of food that is to be collected. On the first day, 20 cans were collected. Then the number of cans increased by 5 each day. If they collected 5 days a week to reach their goal, how many cans of food was their goal per week?"""
    # Define the number of days of collection
    collection_days = 5

    # Define the starting number of cans
    starting_cans = 20

    # Define the daily increase in cans
    daily_increase = 5

    # Calculate the total number of cans collected in a week
    total_cans = starting_cans + (daily_increase * (collection_days - 1))

    # return the result
    result = total_cans
    return result

print(solution())
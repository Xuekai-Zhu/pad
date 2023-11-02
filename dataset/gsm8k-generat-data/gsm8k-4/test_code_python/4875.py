def solution():
    """Tony drinks 72 ounces of water per day. He decides that to stop wasting plastic, he will buy a reusable metal bottle. If he buys an 84-ounce water bottle, how many times will he fill it each week?"""
    # Define the number of ounces Tony drinks per day
    ounces_per_day = 72

    # Define the capacity of the reusable water bottle
    bottle_capacity = 84

    # Calculate the number of times Tony will fill the water bottle each week
    fills_per_week = ((ounces_per_day * 7) / bottle_capacity)

    # Round the result to the nearest integer
    fills_per_week = round(fills_per_week)

    result = fills_per_week
    return result

print(solution())
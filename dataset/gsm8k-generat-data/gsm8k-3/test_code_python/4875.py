def solution():
    """Tony drinks 72 ounces of water per day. He decides that to stop wasting plastic, he will buy a reusable metal bottle. If he buys an 84-ounce water bottle, how many times will he fill it each week?"""
    # Define how much water Tony drinks per week
    WEEKLY_WATER_CONSUMPTION = 72 * 7

    # Calculate how many times Tony will fill the water bottle each week
    fill_times = WEEKLY_WATER_CONSUMPTION // 84

    # Display the number of times Tony will fill the water bottle each week
    result = fill_times
    return result

print(solution())
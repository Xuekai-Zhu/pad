def solution():
    """Lisa is looking to attempt a World Record. She has decided to try and match Joey Chestnut's record of eating 75 full hotdogs, buns included, in 10 minutes. Halfway through the time Lisa has eaten 20 hotdogs. How many hotdogs will she have to eat per minute to at least tie Joey Chestnut's record?"""
    # Define the time and goal number of hotdogs
    TIME = 10 # minutes
    GOAL_HOTDOGS = 75

    # Calculate the halfway mark in time and number of hotdogs
    HALFWAY_TIME = TIME / 2
    HALFWAY_HOTDOGS = GOAL_HOTDOGS / 2

    # Calculate how many hotdogs Lisa has left to eat
    hotdogs_left = GOAL_HOTDOGS - 20

    # Calculate how many hotdogs Lisa needs to eat per minute
    hotdogs_per_minute = hotdogs_left / (HALFWAY_TIME)

    # Round up to the nearest whole hotdog per minute
    hotdogs_per_minute = round(hotdogs_per_minute + 0.5)

    # return the result
    result = hotdogs_per_minute
    return result

print(solution())
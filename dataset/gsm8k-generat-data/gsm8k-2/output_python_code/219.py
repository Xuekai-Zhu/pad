def solution():
    """Lisa is looking to attempt a World Record. She has decided to try and match Joey Chestnut's record of eating 75 full hotdogs, buns included, in 10 minutes. Halfway through the time Lisa has eaten 20 hotdogs. How many hotdogs will she have to eat per minute to at least tie Joey Chestnut's record?"""
    time_remaining = 5
    hotdogs_remaining = 75 - 20
    hotdogs_per_minute = hotdogs_remaining / time_remaining
    result = hotdogs_per_minute
    return result

print(solution())
def solution():
    """Lisa is looking to attempt a World Record. She has decided to try and match Joey Chestnut's record of eating 75 full hotdogs, buns included, in 10 minutes. Halfway through the time Lisa has eaten 20 hotdogs. How many hotdogs will she have to eat per minute to at least tie Joey Chestnut's record?"""
    
    # total time in minutes
    total_time = 10
    
    # halfway time in minutes
    halfway_time = total_time / 2
    
    # number of hotdogs eaten so far
    current_hotdogs = 20
    
    # hotdogs left to eat to tie the record
    hotdogs_left = 75 - current_hotdogs
    
    # time left in minutes
    time_left = halfway_time
    
    # hotdogs per minute needed to tie the record
    hotdogs_per_minute = hotdogs_left / time_left
    
    result = hotdogs_per_minute
    return result

print(solution())
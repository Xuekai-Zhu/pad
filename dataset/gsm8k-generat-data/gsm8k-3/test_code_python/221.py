def solution():
    """Lisa is looking to attempt a World Record. She has decided to try and match Joey Chestnut's record of eating 75 full hotdogs, buns included, in 10 minutes. Halfway through the time Lisa has eaten 20 hotdogs. How many hotdogs will she have to eat per minute to at least tie Joey Chestnut's record?"""
    
    # Define the total number of hotdogs Lisa needs to eat
    TOTAL_HOTDOGS = 75
    
    # Define the amount of time Lisa has to eat the hotdogs in minutes
    TIME = 10
    
    # Calculate the number of hotdogs Lisa has left to eat
    hotdogs_left = TOTAL_HOTDOGS - 20
    
    # Calculate the number of hotdogs Lisa needs to eat per minute to tie Joey Chestnut's record
    hotdogs_per_minute = hotdogs_left / (TIME / 2)
    
    # Display the result
    result = hotdogs_per_minute
    return result

print(solution())
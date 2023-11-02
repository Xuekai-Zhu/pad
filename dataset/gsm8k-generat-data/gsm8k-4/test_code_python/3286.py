def solution():
    """John decides to get a new phone number and it ends up being a recycled number. He used to get 20 text messages a day.
    Now he is getting 55. Assuming the number of texts his friends send has not changed,
    how many text messages per week is he getting that are not intended for him?"""
    
    #Calculate the number of unintended text messages per day
    unintended_messages_per_day = 55 - 20
    
    #Calculate the number of unintended text messages per week
    unintended_messages_per_week = unintended_messages_per_day * 7
    
    result = unintended_messages_per_week
    return result

print(solution())
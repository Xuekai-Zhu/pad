def solution():
    """It takes 15 minutes for Dante to go to Hidden Lake. From Hidden Lake, he has to walk back to the Park Office and it takes him 7 minutes. When he arrives there, he will have been gone from the Park Office 32 minutes altogether. If he had walked to the Lake Park restaurant from the Park office before taking the 15 minute walk to Hidden Lake, how long is the walk from Park Office to the Lake Park restaurant?"""
    total_time = 32
    hidden_lake_time = 15
    to_office_time = 7
    remaining_time = total_time - hidden_lake_time - to_office_time
    restaurant_time = remaining_time / 2
    result = restaurant_time
    return result

print(solution())
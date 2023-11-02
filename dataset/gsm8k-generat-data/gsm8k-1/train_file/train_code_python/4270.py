def solution():
    """It takes 15 minutes for Dante to go to Hidden Lake. From Hidden Lake, 
    he has to walk back to the Park Office and it takes him 7 minutes. When 
    he arrives there, he will have been gone from the Park Office 32 minutes 
    altogether. If he had walked to the Lake Park restaurant from the Park office 
    before taking the 15 minute walk to Hidden Lake, how long is the walk from 
    Park Office to the Lake Park restaurant?"""
    total_time = 32
    to_lake_time = 15
    back_to_office_time = 7
    walking_time_to_lake_restaurant = total_time - to_lake_time - back_to_office_time
    result = walking_time_to_lake_restaurant
    return result

print(solution())